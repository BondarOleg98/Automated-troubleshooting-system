from pandastable import Table
import tkinter
from tkinter import *
import data_analyze_layer.data_processing_module as dpm


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
        self.resizable(False, False)
        self.var.set(0)

        frame = tkinter.Frame(self)
        pt = Table(frame, dataframe=dpm.read_file(self.file), height=400)
        pt.show()
        frame.pack(fill='both')

    def exit_window(self):
        self.destroy()
