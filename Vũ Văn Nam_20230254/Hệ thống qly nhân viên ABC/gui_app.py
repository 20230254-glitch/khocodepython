import tkinter as tk
from tkinter import ttk, messagebox

from models import Manager, Developer, Intern
from services import Company
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

labels = ["ID", "Tên", "Tuổi", "Email", "Lương", "Loại"]
entries = []

for i, text in enumerate(labels):
    tk.Label(frame, text=text).grid(row=i, column=0)
    entry = tk.Entry(frame)
    entry.grid(row=i, column=1)
    entries.append(entry)

entry_id, entry_name, entry_age, entry_email, entry_salary, _ = entries

combo = ttk.Combobox(frame, values=["Manager", "Developer", "Intern"])
combo.grid(row=5, column=1)
combo.current(0)

columns = ("ID", "Tên", "Loại", "Lương")
tree = ttk.Treeview(tab1, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True)


def refresh():
    tree.delete(*tree.get_children())
    for e in company.employees:
        tree.insert("", "end", values=(
            e.emp_id,
            e.name,
            e.__class__.__name__,
            f"{e.calculate_salary():,.0f} VNĐ"
        ))


def add_emp():
    try:
        emp_id = entry_id.get().strip()
        name = entry_name.get().strip()
        age = int(entry_age.get())
        email = entry_email.get().strip()
        salary = float(entry_salary.get())

        if not emp_id or not name:
            raise ValueError("Thiếu dữ liệu")

        if combo.get() == "Manager":
            emp = Manager(emp_id, name, age, email, salary)
        elif combo.get() == "Developer":
            emp = Developer(emp_id, name, age, email, salary, "Python")
        else:
            emp = Intern(emp_id, name, age, email, salary)

        company.add_employee(emp)
        refresh()
        messagebox.showinfo("OK", "Thêm thành công")

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


def delete_emp():
    try:
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Chọn", "Chọn nhân viên")
            return

        emp_id = str(tree.item(selected[0])["values"][0]).strip()
        company.remove_employee(emp_id)
        refresh()
        messagebox.showinfo("OK", "Đã xóa")

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


tk.Button(tab1, text="Thêm", command=add_emp).pack(side="left", padx=10)
tk.Button(tab1, text="Xóa", command=delete_emp).pack(side="left")

# ================= TAB 2: TÌM KIẾM =================
tab2 = tk.Frame(notebook)
notebook.add(tab2, text="Tìm kiếm")

tk.Label(tab2, text="Nhập tên").pack()
search_entry = tk.Entry(tab2)
search_entry.pack()

search_tree = ttk.Treeview(tab2, columns=columns, show="headings")
for col in columns:
    search_tree.heading(col, text=col)
search_tree.pack(fill="both", expand=True)


def search():
    search_tree.delete(*search_tree.get_children())
    keyword = search_entry.get().strip().lower()

    for e in company.employees:
        if keyword in e.name.lower():
            search_tree.insert("", "end", values=(
                e.emp_id,
                e.name,
                e.__class__.__name__,
                f"{e.calculate_salary():,.0f} VNĐ"
            ))


tk.Button(tab2, text="Tìm", command=search).pack()

# ================= TAB 3: LƯƠNG =================
tab3 = tk.Frame(notebook)
notebook.add(tab3, text="Lương")


def show_total():
    total = total_salary(company.employees)
    messagebox.showinfo("Tổng lương", f"{total:,.0f} VNĐ")


def show_top3():
    top = top_3_salary(company.employees)

    if not top:
        messagebox.showwarning("Thông báo", "Chưa có dữ liệu")
        return

    msg = "\n".join(
        [f"{e.name}: {e.calculate_salary():,.0f} VNĐ" for e in top]
    )

    messagebox.showinfo("Top 3 lương", msg)


tk.Button(tab3, text="Tổng lương", command=show_total).pack()
tk.Button(tab3, text="Top 3", command=show_top3).pack()

# ================= TAB 4: DỰ ÁN =================
tab4 = tk.Frame(notebook)
notebook.add(tab4, text="Dự án")

tk.Label(tab4, text="ID nhân viên").pack()
entry_proj_id = tk.Entry(tab4)
entry_proj_id.pack()

tk.Label(tab4, text="Tên dự án").pack()
entry_proj = tk.Entry(tab4)
entry_proj.pack()

proj_list = tk.Listbox(tab4)
proj_list.pack(fill="both", expand=True)


def load_projects():
    try:
        emp = company.find_by_id(entry_proj_id.get().strip())
        proj_list.delete(0, tk.END)
        for p in emp.projects:
            proj_list.insert(tk.END, p)
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


def add_proj():
    try:
        company.assign_project(entry_proj_id.get().strip(), entry_proj.get().strip())
        load_projects()
        messagebox.showinfo("OK", "Đã thêm dự án")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


def remove_proj():
    try:
        emp_id = entry_proj_id.get().strip()
        selected = proj_list.curselection()

        if not selected:
            messagebox.showwarning("Chọn", "Chọn dự án")
            return

        project = proj_list.get(selected[0])
        company.remove_project(emp_id, project)
        load_projects()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


tk.Button(tab4, text="Xem", command=load_projects).pack()
tk.Button(tab4, text="Thêm", command=add_proj).pack()
tk.Button(tab4, text="Xóa", command=remove_proj).pack()

# ================= TAB 5: HIỆU SUẤT =================
tab5 = tk.Frame(notebook)
notebook.add(tab5, text="Hiệu suất")

tk.Label(tab5, text="ID").pack()
entry_perf_id = tk.Entry(tab5)
entry_perf_id.pack()

tk.Label(tab5, text="Điểm (0-10)").pack()
entry_perf = tk.Entry(tab5)
entry_perf.pack()


def update_perf():
    try:
        score = float(entry_perf.get())

        if score < 0 or score > 10:
            raise ValueError("Điểm phải từ 0-10")

        company.update_performance(entry_perf_id.get().strip(), score)
        refresh()
        messagebox.showinfo("OK", "Đã cập nhật")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


tk.Button(tab5, text="Cập nhật", command=update_perf).pack()

# ================= TAB 6: NHÂN SỰ =================
tab6 = tk.Frame(notebook)
notebook.add(tab6, text="Nhân sự")

tk.Label(tab6, text="ID nhân viên").pack()
entry_hr = tk.Entry(tab6)
entry_hr.pack()


def promote():
    try:
        company.promote(entry_hr.get().strip())
        refresh()
        messagebox.showinfo("OK", "Thăng chức thành công")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


def remove_emp_hr():
    try:
        company.remove_employee(entry_hr.get().strip())
        refresh()
        messagebox.showinfo("OK", "Đã xóa nhân viên")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


tk.Button(tab6, text="Thăng chức", command=promote).pack()
tk.Button(tab6, text="Xóa NV", command=remove_emp_hr).pack()

# ================= TAB 7: THỐNG KÊ =================
tab7 = tk.Frame(notebook)
notebook.add(tab7, text="Thống kê")


def stats():
    try:
        if not company.employees:
            messagebox.showwarning("Thông báo", "Chưa có dữ liệu")
            return

        count = count_by_type(company.employees)
        total = total_salary(company.employees)
        avg = avg_projects(company.employees)

        msg = f"""
Manager: {count.get('Manager',0)}
Developer: {count.get('Developer',0)}
Intern: {count.get('Intern',0)}

Tổng lương: {total:,.0f} VNĐ
TB dự án: {avg:.2f}
"""
        messagebox.showinfo("Thống kê", msg)

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


tk.Button(tab7, text="Xem thống kê", command=stats).pack()

# ================= RUN =================
root.mainloop()