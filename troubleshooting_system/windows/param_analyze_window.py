import tkinter
import troubleshooting_system.windows.chart_window as cw
from tkinter import *


class ParamAnalyzeWindow(tkinter.Toplevel):
    def __init__(self, root, param):
        super().__init__(root)
        self.root = root
        self.flag = StringVar()
        self.col_name = StringVar()
        self.fail_col_name = StringVar()
        self.init_param_analyze_window(param)
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_param_analyze_window(self, param):
        self.flag.set(NORMAL)
        self.title("Param window")
        self.geometry("300x180+300+200")
        self.resizable(False, False)

        if param <= 2:
            self.flag.set(NORMAL)
        else:
            self.flag.set(DISABLED)

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_submit = tkinter.Button(self, text="Submit", anchor=SW, padx=10, command=self.choose_chart)
        btn_submit.place(x=230, y=150)
        btn_back.place(x=3, y=150)

        file_label = Label(self, text="Choose param for chart(plot)", font="Arial 12", pady=15)
        file_label.pack()

        param_col_entry = Entry(self, textvariable=self.col_name)
        param_col_entry.pack()

        param_fail_entry = Entry(self, textvariable=self.fail_col_name, state=self.flag.get())
        param_fail_entry.pack()

    def choose_chart(self):
        cw.ChartWindow(self)
        self.withdraw()

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
