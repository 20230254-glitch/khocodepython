import tkinter as tk
from view.main_view import MainView
from controller.main_controller import MainController

def main():
    root = tk.Tk()

    view = MainView(root)
    controller = MainController(view)

    view.set_controller(controller)

    root.mainloop()

if __name__ == "__main__":
    main()