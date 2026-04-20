import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ================= DB =================
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    job TEXT,
    dept_id INTEGER,
    salary REAL
)
""")
conn.commit()

# seed data
cursor.execute("SELECT COUNT(*) FROM employee")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
        INSERT INTO employee VALUES (?,?,?,?,?)
    """, [
        (1,'CLARK','MANAGER',10,3000),
        (2,'MILLER','CLERK',10,1500),
        (3,'JOHN','MANAGER',20,4000)
    ])
    conn.commit()

# ================= UI =================
root = tk.Tk()
root.title("EMPLOYEE MANAGEMENT SYSTEM")
root.geometry("1000x500")
root.configure(bg="#f4f6f9")

# ================= LEFT TABLE =================
left_frame = tk.Frame(root, bg="white")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

cols = ("ID","Name","Job","Dept","Salary")
tree = ttk.Treeview(left_frame, columns=cols, show="headings")

for c in cols:
    tree.heading(c, text=c)
    tree.column(c, width=120)

tree.pack(fill=tk.BOTH, expand=True)

# ================= RIGHT FORM =================
right_frame = tk.Frame(root, bg="#f4f6f9")
right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

tk.Label(right_frame, text="EMPLOYEE FORM", font=("Arial",14,"bold"), bg="#f4f6f9").pack(pady=10)

def make_entry(label):
    tk.Label(right_frame, text=label, bg="#f4f6f9").pack()
    e = tk.Entry(right_frame, width=30)
    e.pack(pady=5)
    return e

e_id = make_entry("ID")
e_name = make_entry("Name")
e_job = make_entry("Job")
e_dept = make_entry("Dept")
e_salary = make_entry("Salary")

# ================= FUNCTIONS =================
def refresh():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM employee")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def clear():
    e_id.delete(0, tk.END)
    e_name.delete(0, tk.END)
    e_job.delete(0, tk.END)
    e_dept.delete(0, tk.END)
    e_salary.delete(0, tk.END)

def add():
    cursor.execute("INSERT INTO employee VALUES (?,?,?,?,?)",
                   (e_id.get(), e_name.get(), e_job.get(), e_dept.get(), e_salary.get()))
    conn.commit()
    refresh()
    clear()

def update():
    cursor.execute("""
        UPDATE employee
        SET name=?, job=?, dept_id=?, salary=?
        WHERE emp_id=?
    """, (e_name.get(), e_job.get(), e_dept.get(), e_salary.get(), e_id.get()))
    conn.commit()
    refresh()

def delete():
    cursor.execute("DELETE FROM employee WHERE emp_id=?", (e_id.get(),))
    conn.commit()
    refresh()
    clear()

def on_select(event):
    selected = tree.focus()
    data = tree.item(selected)['values']
    if data:
        clear()
        e_id.insert(0, data[0])
        e_name.insert(0, data[1])
        e_job.insert(0, data[2])
        e_dept.insert(0, data[3])
        e_salary.insert(0, data[4])

tree.bind("<ButtonRelease-1>", on_select)

# ================= BUTTONS =================
btn_frame = tk.Frame(right_frame, bg="#f4f6f9")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Add", width=10, bg="green", fg="white", command=add).grid(row=0,column=0,padx=5)
tk.Button(btn_frame, text="Update", width=10, bg="blue", fg="white", command=update).grid(row=0,column=1,padx=5)
tk.Button(btn_frame, text="Delete", width=10, bg="red", fg="white", command=delete).grid(row=0,column=2,padx=5)
tk.Button(btn_frame, text="Refresh", width=10, command=refresh).grid(row=0,column=3,padx=5)

# ================= LOAD =================
refresh()

root.mainloop()