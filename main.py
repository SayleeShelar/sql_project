import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class EmployeeManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System - SQL Demo")
        self.root.geometry("800x600")
        
        self.conn = sqlite3.connect('company.db')
        self.cursor = self.conn.cursor()
        self.init_db()
        
        self.setup_gui()
        
    def init_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                salary REAL NOT NULL
            )
        ''')
        # Sample data
        self.cursor.execute("SELECT COUNT(*) FROM employees")
        if self.cursor.fetchone()[0] == 0:
            samples = [
                ('John Doe', 'Developer', 75000),
                ('Jane Smith', 'Manager', 95000),
                ('Bob Johnson', 'Analyst', 65000)
            ]
            self.cursor.executemany("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", samples)
            self.conn.commit()
        self.conn.commit()
        
    def setup_gui(self):
        # Notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # CRUD Tab
        crud_frame = ttk.Frame(notebook)
        notebook.add(crud_frame, text='Employees CRUD')
        
        # List
        tree_frame = ttk.Frame(crud_frame)
        tree_frame.pack(fill='both', expand=True, pady=(0,10))
        self.tree = ttk.Treeview(tree_frame, columns=('ID', 'Name', 'Position', 'Salary'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Position', text='Position')
        self.tree.heading('Salary', text='Salary')
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Form
        form_frame = ttk.LabelFrame(crud_frame, text='Employee Form')
        form_frame.pack(fill='x', pady=(0,10))
        
        ttk.Label(form_frame, text='Name:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.name_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text='Position:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.pos_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.pos_var).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text='Salary:').grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.salary_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.salary_var).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(form_frame, text='Add', command=self.add_employee).grid(row=3, column=0, pady=10)
        ttk.Button(form_frame, text='Edit', command=self.edit_employee).grid(row=3, column=1, pady=10)
        ttk.Button(form_frame, text='Delete', command=self.delete_employee).grid(row=3, column=2, pady=10)
        ttk.Button(form_frame, text='Refresh', command=self.refresh_list).grid(row=3, column=3, pady=10)
        
        self.refresh_list()
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        
        # Query Tab
        query_frame = ttk.Frame(notebook)
        notebook.add(query_frame, text='Custom SQL Query')
        
        ttk.Label(query_frame, text='SQL Query:').pack(anchor='w', padx=10, pady=5)
        self.query_text = scrolledtext.ScrolledText(query_frame, height=10, width=80)
        self.query_text.pack(padx=10, pady=5, fill='both', expand=True)
        
        # Sample query
        self.query_text.insert('1.0', 'SELECT * FROM employees WHERE salary > 70000;')
        
        ttk.Button(query_frame, text='Execute Query', command=self.execute_query).pack(pady=10)
        self.result_text = scrolledtext.ScrolledText(query_frame, height=8, width=80, state='disabled')
        self.result_text.pack(padx=10, pady=5, fill='both')
    
    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.cursor.execute("SELECT * FROM employees")
        for row in self.cursor.fetchall():
            self.tree.insert('', 'end', values=row)
    
    def on_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            self.name_var.set(values[1])
            self.pos_var.set(values[2])
            self.salary_var.set(values[3])
    
    def add_employee(self):
        if not all([self.name_var.get(), self.pos_var.get(), self.salary_var.get()]):
            messagebox.showerror("Error", "Fill all fields")
            return
        try:
            self.cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)",
                               (self.name_var.get(), self.pos_var.get(), float(self.salary_var.get())))
            self.conn.commit()
            self.refresh_list()
            self.clear_form()
            messagebox.showinfo("Success", "Employee added")
        except ValueError:
            messagebox.showerror("Error", "Invalid salary (use number)")
    
    def edit_employee(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showerror("Error", "Select an employee")
            return
        if not all([self.name_var.get(), self.pos_var.get(), self.salary_var.get()]):
            messagebox.showerror("Error", "Fill all fields")
            return
        try:
            item = self.tree.item(selection[0])
            emp_id = item['values'][0]
            self.cursor.execute("UPDATE employees SET name=?, position=?, salary=? WHERE id=?",
                               (self.name_var.get(), self.pos_var.get(), float(self.salary_var.get()), emp_id))
            self.conn.commit()
            self.refresh_list()
            self.clear_form()
            messagebox.showinfo("Success", "Employee updated")
        except ValueError:
            messagebox.showerror("Error", "Invalid salary")
    
    def delete_employee(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showerror("Error", "Select an employee")
            return
        item = self.tree.item(selection[0])
        emp_id = item['values'][0]
        if messagebox.askyesno("Confirm", "Delete this employee?"):
            self.cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
            self.conn.commit()
            self.refresh_list()
            self.clear_form()
    
    def clear_form(self):
        self.name_var.set('')
        self.pos_var.set('')
        self.salary_var.set('')
    
    def execute_query(self):
        query = self.query_text.get('1.0', tk.END).strip()
        if not query:
            messagebox.showerror("Error", "Enter a SQL query")
            return
        try:
            self.cursor.execute(query)
            if query.strip().upper().startswith('SELECT'):
                results = self.cursor.fetchall()
                columns = [desc[0] for desc in self.cursor.description]
                result_str = f"Columns: {', '.join(columns)}\n\n"
                result_str += '\n'.join([str(row) for row in results])
            else:
                self.conn.commit()
                result_str = "Query executed successfully (no results for non-SELECT)."
            self.result_text.config(state='normal')
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert('1.0', result_str)
            self.result_text.config(state='disabled')
        except sqlite3.Error as e:
            messagebox.showerror("SQL Error", str(e))
    
    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManager(root)
    root.mainloop()
