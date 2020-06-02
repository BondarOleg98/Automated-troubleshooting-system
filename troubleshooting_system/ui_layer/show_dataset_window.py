from tkinter import messagebox

from pandastable import Table
import tkinter
from tkinter import *
import troubleshooting_system.data_science_layer.analyze_module as ad


class DataWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.var = IntVar()
        self.root = root
        self.file = file
        self.init_data_window()
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_data_window(self):
        self.title("Dataset window")
        self.geometry("600x400+300+200")
        self.focus_get()
        self.resizable(False, False)
        self.var.set(0)

        frame = tkinter.Frame(self)
        pt = Table(frame, dataframe=ad.read_file(self.file), height=400)
        pt.show()
        frame.pack(fill='both')

    def exit_window(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.quit()

