import tkinter as tk
from tkinter import filedialog, messagebox

# ================== DICTIONARY ==================
base_dict = {'a':'!', 'b':'@', 'c':'#', 'd':'$'}

code_dict = {}
for k, v in base_dict.items():
    code_dict[k] = v
    code_dict[k.upper()] = v

decode_dict = {v: k for k, v in code_dict.items()}

def dict_encode(text):
    return "".join(code_dict.get(ch, ch) for ch in text)

def dict_decode(text):
    return "".join(decode_dict.get(ch, ch) for ch in text)


# ================== CAESAR ==================
def caesar_encode(text, k):
    result = ""
    for ch in text:
        if ch.isalpha():
            shift = k % 26
            if ch.islower():
                result += chr((ord(ch) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch
    return result

def caesar_decode(text, k):
    return caesar_encode(text, -k)


# ================== VIGENERE ==================
def vigenere_encode(text, key):
    result = ""
    key = key.lower()
    j = 0

    for ch in text:
        if ch.isalpha():
            k = ord(key[j % len(key)]) - 97
            if ch.islower():
                result += chr((ord(ch) - 97 + k) % 26 + 97)
            else:
                result += chr((ord(ch) - 65 + k) % 26 + 65)
            j += 1
        else:
            result += ch
    return result

def vigenere_decode(text, key):
    result = ""
    key = key.lower()
    j = 0

    for ch in text:
        if ch.isalpha():
            k = ord(key[j % len(key)]) - 97
            if ch.islower():
                result += chr((ord(ch) - 97 - k) % 26 + 97)
            else:
                result += chr((ord(ch) - 65 - k) % 26 + 65)
            j += 1
        else:
            result += ch
    return result


# ================== FILE ==================
def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ================== GUI ==================
def choose_file():
    path = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, path)

    if path:
        text = read_file(path)
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, text)


def process(mode):
    try:
        text = input_text.get("1.0", tk.END)
        method = method_var.get()

        if method == "Dictionary":
            result = dict_encode(text) if mode == "encode" else dict_decode(text)

        elif method == "Caesar":
            shift = int(entry_key.get())
            result = caesar_encode(text, shift) if mode == "encode" else caesar_decode(text, shift)

        elif method == "Vigenere":
            key = entry_key.get()
            if not key:
                messagebox.showerror("Lỗi", "Nhập key!")
                return
            result = vigenere_encode(text, key) if mode == "encode" else vigenere_decode(text, key)

        # Hiển thị kết quả lên GUI
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


def save_file():
    try:
        content = output_text.get("1.0", tk.END)
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            write_file(path, content)
            messagebox.showinfo("Thành công", "Đã lưu file!")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


# ================== WINDOW ==================
root = tk.Tk()
root.title("Mã hóa / Giải mã văn bản")
root.geometry("700x500")

# File
tk.Label(root, text="Chọn file:").pack()
entry_file = tk.Entry(root, width=60)
entry_file.pack()
tk.Button(root, text="Browse", command=choose_file).pack()

# Method
method_var = tk.StringVar(value="Dictionary")
tk.Label(root, text="Phương pháp:").pack()

tk.Radiobutton(root, text="Dictionary", variable=method_var, value="Dictionary").pack()
tk.Radiobutton(root, text="Caesar", variable=method_var, value="Caesar").pack()
tk.Radiobutton(root, text="Vigenere", variable=method_var, value="Vigenere").pack()

# Key
tk.Label(root, text="Key / Shift:").pack()
entry_key = tk.Entry(root)
entry_key.pack()

# Buttons
frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

tk.Button(frame_btn, text="Mã hóa", command=lambda: process("encode"), bg="green", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Giải mã", command=lambda: process("decode"), bg="blue", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Lưu file", command=save_file, bg="orange").grid(row=0, column=2, padx=5)

# Text area
tk.Label(root, text="Nội dung INPUT:").pack()
input_text = tk.Text(root, height=10)
input_text.pack(fill="both", expand=True)

tk.Label(root, text="Kết quả OUTPUT:").pack()
output_text = tk.Text(root, height=10)
output_text.pack(fill="both", expand=True)

root.mainloop()