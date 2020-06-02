import tkinter
from tkinter import messagebox

import troubleshooting_system.ui_layer.result_prediction_window as rpw
import troubleshooting_system.data_analyze_layer.prediction_module as pd
import troubleshooting_system.data_analyze_layer.data_processing_module as dpm
from tkinter import *


class ParamPredictionWindow(tkinter.Toplevel):
    def __init__(self, root, file, algorithm, count, fail_col_name):
        super().__init__(root)
        self.file = file
        self.lst = []
        self.root = root
        self.algorithm = algorithm
        self.fail_col_name = fail_col_name
        self.init_param_analyze_window()
        for i in range(int(count)):
            self.lst.append(StringVar())
        self.labels = []
        self.entries = []
        for i in range(int(count)):
            self.labels.append(Label(self, text="[" + str(i + 1) + "]"))
            self.labels[-1].grid(row=i + 1, column=0, sticky=W)
            self.entries.append(Entry(self, textvariable=self.lst[i]))
            self.entries[-1].grid(row=i + 1, column=0, sticky=W, padx=20)
        if len(self.lst) > 0:
            btn_submit = tkinter.Button(self, text="Submit", command=self.prediction, anchor=SW, padx=10)
            btn_submit.place(x=235, y=200)
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_param_analyze_window(self):
        if self.algorithm == 1:
            self.title("Random forest")
        else:
            self.title("Logical regression")
        self.grab_set()
        self.focus_set()
        self.geometry("305x230+300+200")

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_back.place(x=3, y=200)

        title_label = Label(self, text="Enter name of columns for predict", font="Arial 15")
        title_label.grid(row=0, column=0, sticky=W, pady=15)

    def prediction(self):
        params = []
        for el in self.lst:
            params.append(el.get())
        try:
            flag = pd.prediction(dpm.read_file_prediction(self.file), params, self.fail_col_name, self.algorithm)
            if flag is None:
                raise Exception("Please, enter correct name of column")
            rpw.ResultPredictionWindow(self, dpm.read_file_prediction(self.file), params, self.fail_col_name,
                                       self.algorithm, self.file)
            self.withdraw()
        except Exception as e:
            messagebox.showerror(title="Error", message=e)

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
