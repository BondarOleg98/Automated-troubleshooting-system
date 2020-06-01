from pandastable import Table
import tkinter
from tkinter import *
import troubleshooting_system.functions.analyze_data as ad


class DataWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.var = IntVar()
        self.root = root
        self.file = file
        self.init_functional_window()
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_functional_window(self):
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
        self.destroy()

