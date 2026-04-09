import tkinter as tk
from tkinter import ttk, messagebox

from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from services.payroll import *

company = Company()

# ================= WINDOW =================
root = tk.Tk()
root.title("Hệ thống quản lý nhân viên")
root.geometry("1000x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ================= TAB 1: NHÂN VIÊN =================
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Nhân viên")

frame = tk.Frame(tab1)
frame.pack()

entry_id = tk.Entry(frame)
entry_name = tk.Entry(frame)
entry_age = tk.Entry(frame)
entry_email = tk.Entry(frame)
entry_salary = tk.Entry(frame)

combo = ttk.Combobox(frame, values=["Manager", "Developer", "Intern"])
combo.current(0)

tk.Label(frame, text="ID").grid(row=0, column=0)
entry_id.grid(row=0, column=1)

tk.Label(frame, text="Tên").grid(row=1, column=0)
entry_name.grid(row=1, column=1)

tk.Label(frame, text="Tuổi").grid(row=2, column=0)
entry_age.grid(row=2, column=1)

tk.Label(frame, text="Email").grid(row=3, column=0)
entry_email.grid(row=3, column=1)

tk.Label(frame, text="Lương").grid(row=4, column=0)
entry_salary.grid(row=4, column=1)

tk.Label(frame, text="Loại").grid(row=5, column=0)
combo.grid(row=5, column=1)

columns = ("ID", "Tên", "Loại", "Lương")
tree = ttk.Treeview(tab1, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True)

def refresh():
    tree.delete(*tree.get_children())
    for e in company.employees:
        tree.insert("", "end", values=(e.emp_id, e.name, e.__class__.__name__, e.calculate_salary()))

def add_emp():
    try:
        if combo.get() == "Manager":
            emp = Manager(entry_id.get(), entry_name.get(), int(entry_age.get()), entry_email.get(), float(entry_salary.get()))
        elif combo.get() == "Developer":
            emp = Developer(entry_id.get(), entry_name.get(), int(entry_age.get()), entry_email.get(), float(entry_salary.get()), "Python")
        else:
            emp = Intern(entry_id.get(), entry_name.get(), int(entry_age.get()), entry_email.get(), float(entry_salary.get()))

        company.add_employee(emp)
        refresh()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def delete_emp():
    try:
        item = tree.selection()[0]
        emp_id = tree.item(item)["values"][0]
        company.remove_employee(emp_id)
        refresh()
    except:
        pass

tk.Button(tab1, text="Thêm", command=add_emp).pack(side="left", padx=10)
tk.Button(tab1, text="Xóa", command=delete_emp).pack(side="left")

# ================= TAB 2: TÌM KIẾM =================
tab2 = tk.Frame(notebook)
notebook.add(tab2, text="Tìm kiếm")

search_entry = tk.Entry(tab2)
search_entry.pack()

def search():
    tree.delete(*tree.get_children())
    for e in company.employees:
        if search_entry.get().lower() in e.name.lower():
            tree.insert("", "end", values=(e.emp_id, e.name, e.__class__.__name__, e.calculate_salary()))

tk.Button(tab2, text="Tìm", command=search).pack()

# ================= TAB 3: LƯƠNG =================
tab3 = tk.Frame(notebook)
notebook.add(tab3, text="Lương")

def show_total():
    messagebox.showinfo("Tổng lương", str(total_salary(company.employees)))

def show_top3():
    top = top_3_salary(company.employees)
    msg = "\n".join([f"{e.name}: {e.calculate_salary()}" for e in top])
    messagebox.showinfo("Top 3", msg)

tk.Button(tab3, text="Tổng lương", command=show_total).pack()
tk.Button(tab3, text="Top 3", command=show_top3).pack()

# ================= TAB 4: DỰ ÁN =================
tab4 = tk.Frame(notebook)
notebook.add(tab4, text="Dự án")

entry_proj_id = tk.Entry(tab4)
entry_proj = tk.Entry(tab4)

entry_proj_id.pack()
entry_proj.pack()

def add_proj():
    company.assign_project(entry_proj_id.get(), entry_proj.get())

tk.Button(tab4, text="Thêm dự án", command=add_proj).pack()

# ================= TAB 5: HIỆU SUẤT =================
tab5 = tk.Frame(notebook)
notebook.add(tab5, text="Hiệu suất")

entry_perf_id = tk.Entry(tab5)
entry_perf = tk.Entry(tab5)

entry_perf_id.pack()
entry_perf.pack()

def update_perf():
    company.update_performance(entry_perf_id.get(), float(entry_perf.get()))

tk.Button(tab5, text="Cập nhật", command=update_perf).pack()

# ================= TAB 6: NHÂN SỰ =================
tab6 = tk.Frame(notebook)
notebook.add(tab6, text="Nhân sự")

entry_hr = tk.Entry(tab6)
entry_hr.pack()

def promote():
    company.promote(entry_hr.get())

tk.Button(tab6, text="Thăng chức", command=promote).pack()

# ================= TAB 7: THỐNG KÊ =================
tab7 = tk.Frame(notebook)
notebook.add(tab7, text="Thống kê")

def stats():
    msg = str(count_by_type(company.employees))
    messagebox.showinfo("Thống kê", msg)

tk.Button(tab7, text="Xem thống kê", command=stats).pack()

# ================= RUN =================
root.mainloop()