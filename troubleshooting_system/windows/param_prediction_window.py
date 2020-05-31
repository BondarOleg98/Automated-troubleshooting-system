import tkinter
import troubleshooting_system.windows.chart_window as cw
from tkinter import *


class ParamPredictionWindow(tkinter.Toplevel):
    def __init__(self, root, algorithm, count, fail_col_name):
        super().__init__(root)
        lst = []
        self.root = root
        self.flag = StringVar()
        self.col_name = StringVar()
        self.init_param_analyze_window(count)
        for i in range(1, count + 1):
            lst.append(param)

        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_param_analyze_window(self, count):
        self.flag.set(NORMAL)
        self.title("Param window")
        self.geometry("300x180+300+200")
        self.resizable(False, False)


        for i in range(1, count + 1):
            Entry(self, textvariable=self.col_name).grid(row=i, column=0, sticky=W, padx=120)

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
