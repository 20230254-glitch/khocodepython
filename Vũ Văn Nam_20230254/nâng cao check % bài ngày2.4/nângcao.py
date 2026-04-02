import os
import difflib
import ast
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import webbrowser
import tempfile


# ===== Đọc file =====
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        return ""


# ===== Đọc toàn bộ code =====
def read_all_code(folder):
    code = ""
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                code += read_file(os.path.join(root, file)) + "\n"
    return code


# ===== So sánh text =====
def similarity_text(code1, code2):
    if not code1 or not code2:
        return 0
    return difflib.SequenceMatcher(None, code1, code2).ratio() * 100


# ===== CHUẨN HÓA AST =====
def normalize_ast(node):
    for child in ast.iter_child_nodes(node):
        normalize_ast(child)

    # Xóa tên biến
    if hasattr(node, 'id'):
        node.id = "VAR"

    # Xóa tên hàm
    if hasattr(node, 'name'):
        node.name = "FUNC"

    return node


def get_structure(code):
    try:
        tree = ast.parse(code)
        tree = normalize_ast(tree)
        return ast.dump(tree)
    except:
        return ""


# ===== So sánh logic =====
def similarity_structure(code1, code2):
    s1 = get_structure(code1)
    s2 = get_structure(code2)
    if not s1 or not s2:
        return 0
    return difflib.SequenceMatcher(None, s1, s2).ratio() * 100


# ===== Lấy danh sách file =====
def get_py_files(folder):
    files = {}
    for root, _, filenames in os.walk(folder):
        for f in filenames:
            if f.endswith(".py"):
                files[f] = os.path.join(root, f)
    return files


# ===== HIỂN THỊ DIFF =====
def show_diff(file1, file2):
    code1 = read_file(file1).splitlines()
    code2 = read_file(file2).splitlines()

    d = difflib.HtmlDiff()
    html = d.make_file(code1, code2, fromdesc=file1, todesc=file2)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    temp_file.write(html.encode("utf-8"))
    temp_file.close()

    webbrowser.open(temp_file.name)


# ===== Chọn file hoặc folder =====
def choose_path(entry):
    path = filedialog.askopenfilename(
        title="Chọn file .py (Cancel để chọn thư mục)",
        filetypes=[("Python files", "*.py")]
    )

    if not path:
        path = filedialog.askdirectory()

    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)


# ===== Kiểm tra hợp lệ =====
def is_valid_path(path):
    return os.path.isfile(path) or os.path.isdir(path)


# ===== So sánh =====
def run_compare():
    path1 = entry1.get().strip()
    path2 = entry2.get().strip()

    if not is_valid_path(path1):
        messagebox.showerror("Lỗi", "Đường dẫn 1 không hợp lệ!")
        return

    if not is_valid_path(path2):
        messagebox.showerror("Lỗi", "Đường dẫn 2 không hợp lệ!")
        return

    # Xóa bảng
    for row in tree.get_children():
        tree.delete(row)

    # ===== SO FILE =====
    if os.path.isfile(path1) and os.path.isfile(path2):
        code1 = read_file(path1)
        code2 = read_file(path2)

        text_sim = similarity_text(code1, code2)
        struct_sim = similarity_structure(code1, code2)

        result = f"=== SO FILE ===\n"
        result += f"Text: {text_sim:.2f}%\n"
        result += f"Logic: {struct_sim:.2f}%\n"

        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, result)

        tree.insert("", "end", values=(
            os.path.basename(path1) + " vs " + os.path.basename(path2),
            f"{text_sim:.2f}%",
            f"{struct_sim:.2f}%",
            "Double click để xem diff"
        ), tags=(path1, path2))

        return

    # ===== SO FOLDER =====
    if os.path.isdir(path1) and os.path.isdir(path2):

        code1 = read_all_code(path1)
        code2 = read_all_code(path2)

        if not code1 or not code2:
            messagebox.showerror("Lỗi", "Không có dữ liệu!")
            return

        text_sim = similarity_text(code1, code2)
        struct_sim = similarity_structure(code1, code2)

        result = f"=== TỔNG THỂ ===\n"
        result += f"Text: {text_sim:.2f}%\n"
        result += f"Logic: {struct_sim:.2f}%\n"

        if text_sim > 80:
            result += " Code gần như giống hệt\n"
        elif struct_sim > 80:
            result += " Trùng cách giải\n"
        elif struct_sim > 65:
            result += " Có dấu hiệu giống\n"
        else:
            result += " Khác nhau\n"

        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, result)

        # ===== Chi tiết từng file =====
        files1 = get_py_files(path1)
        files2 = get_py_files(path2)

        for name in files1:
            if name in files2:
                f1 = files1[name]
                f2 = files2[name]

                code1 = read_file(f1)
                code2 = read_file(f2)

                t = similarity_text(code1, code2)
                s = similarity_structure(code1, code2)

                if t > 85:
                    note = " Copy"
                elif s > 80:
                    note = " Trùng logic"
                elif s > 65:
                    note = " Giống cách làm"
                else:
                    note = "OK"

                tree.insert("", "end", values=(
                    name,
                    f"{t:.2f}%",
                    f"{s:.2f}%",
                    note
                ), tags=(f1, f2))

        return

    messagebox.showerror("Lỗi", "Chọn cùng loại (file-file hoặc folder-folder)")


# ===== CLICK XEM DIFF =====
def on_item_click(event):
    selected = tree.focus()
    if not selected:
        return

    item = tree.item(selected)
    tags = item.get("tags")

    if len(tags) == 2:
        show_diff(tags[0], tags[1])


# ===== GUI =====
root = tk.Tk()
root.title("Tool So Sánh Code Python (Final)")
root.geometry("850x600")

tk.Label(root, text="File/Thư mục 1").pack()
entry1 = tk.Entry(root, width=90)
entry1.pack()
tk.Button(root, text="Chọn", command=lambda: choose_path(entry1)).pack()

tk.Label(root, text="File/Thư mục 2").pack()
entry2 = tk.Entry(root, width=90)
entry2.pack()
tk.Button(root, text="Chọn", command=lambda: choose_path(entry2)).pack()

tk.Button(root, text="So sánh", bg="green", fg="white", command=run_compare).pack(pady=10)

text_result = tk.Text(root, height=6)
text_result.pack(fill="x")

columns = ("File", "Text %", "Logic %", "Đánh giá")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True)

tree.bind("<Double-1>", on_item_click)

root.mainloop()