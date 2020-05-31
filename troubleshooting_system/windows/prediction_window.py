import tkinter
from tkinter import *
import troubleshooting_system.windows.param_prediction_window as ppw

class PredictionWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.algorithm = IntVar()
        self.root = root
        self.file = file
        self.count_data = IntVar()
        self.fail_col_name = StringVar()
        self.init_child()
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_child(self):
        self.title("Prediction window")
        self.geometry("300x300+300+200")
        self.resizable(False, False)
        # self.grab_set()
        # self.focus_set()
        self.algorithm.set(0)

        title_label = Label(self, text="Please enter parameters", font="Arial 15", pady = 15, padx=40)
        title_label.grid(row=1, column=0, sticky=W)

        Label(self, text="Failure column name:").grid(row=2, column=0, sticky=W, pady=2)
        Label(self, text="Count columns:").grid(row=3, column=0, sticky=W, pady =2 )

        param_fail_entry = Entry(self, textvariable=self.fail_col_name)
        param_count_data = Entry(self, textvariable=self.count_data)
        param_fail_entry.grid(row=2, column=0, sticky=W, padx=120)
        param_count_data.grid(row=3, column=0, sticky=W, padx=120)

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_submit = tkinter.Button(self, text="Submit",command=self.open_param_window, anchor=SW, padx=10)
        btn_submit.place(x=230, y=270)
        btn_back.place(x=3, y=270)

        algorithm_label = Label(self, text="Algorithm fo study:", pady=3)
        algorithm_label.grid(row=4, column=0, sticky=W)

        rf = Radiobutton(self, text="Random Forest", variable=self.algorithm, value=1)
        lr = Radiobutton(self, text="Logical regression", variable=self.algorithm, value=2)
        rf.grid(row=5, column=0, sticky=W)
        lr.grid(row=6, column=0, sticky=W)

    def open_param_window(self):
        ppw.ParamPredictionWindow(self, self.algorithm.get(),self.count_data.get(),self.fail_col_name.get())
    def exit_window(self):
        self.destroy()
        self.root.deiconify()
