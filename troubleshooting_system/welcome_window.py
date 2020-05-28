import os
import tkinter
import function_window as fw
from tkinter import filedialog, messagebox
from tkinter import *


class WelcomeWindow(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.icon_img = tkinter.PhotoImage(file="file_icon.gif")
        self.root = root
        self.init_main()
        root.protocol("WM_DELETE_WINDOW", self.exit_system)

    def init_main(self):
        self.menu_window()
        self.root.title("Searching app failures")
        self.root.geometry("650x400+300+100")
        self.root.resizable(False, False)

        welcome_label = Label(text="Welcome to system", font="Arial 32")

        choose_frame = LabelFrame(text="Choose file", height=200, width=200, font="Arial 12")
        # btn = tkinter.Button(choose_frame, command=self.open_dialog, image=self.icon_img)
        # btn.pack()
        temp = "E:\\test.csv"
        fw.FunctionWindow(self.root, temp)
        welcome_label.pack()
        choose_frame.pack()
        self.root.withdraw()

    def open_dialog(self):
        file = filedialog.askopenfilename(
            initialdir='/',
            initialfile='tmp',
            filetypes=[("CSV", "*.csv")])
        if file != "":
            os.startfile(file)
            fw.FunctionWindow(self.root, file)
            self.root.withdraw()

    def menu_window(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Exit", command=self.exit_system)
        menu.add_cascade(label="File", menu=file_menu)

    def exit_system(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.quit()
