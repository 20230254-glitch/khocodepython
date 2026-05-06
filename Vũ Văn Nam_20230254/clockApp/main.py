import tkinter as tk
from ui.main_view import MainView

if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()