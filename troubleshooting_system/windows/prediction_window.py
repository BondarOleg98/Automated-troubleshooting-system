import tkinter
from tkinter import *
from tkinter import messagebox
import troubleshooting_system.functions.prediction_data as pd

import troubleshooting_system.windows.param_prediction_window as ppw


class PredictionWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.algorithm = IntVar()
        self.root = root
        self.file = file
        self.count_data = StringVar()
        self.fail_col_name = StringVar()
        self.init_child()
        self.btn_submit = tkinter.Button(self, text="Submit", command=self.open_param_window, anchor=SW, padx=10,
                                         state=DISABLED)
        self.btn_submit.place(x=230, y=220)
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_child(self):
        self.title("Prediction window")
        self.geometry("300x250+300+200")
        self.resizable(False, False)
        # self.grab_set()
        # self.focus_set()
        self.algorithm.set(0)

        title_label = Label(self, text="Please enter parameters", font="Arial 15", pady=15, padx=40)
        title_label.grid(row=1, column=0, sticky=W)

        Label(self, text="Failure column name").grid(row=2, column=0, sticky=W, pady=2)
        Label(self, text="Count columns").grid(row=3, column=0, sticky=W, pady=2)

        param_fail_entry = Entry(self, textvariable=self.fail_col_name)
        param_count_data = Entry(self, textvariable=self.count_data)
        param_fail_entry.grid(row=2, column=0, sticky=W, padx=120)
        param_count_data.grid(row=3, column=0, sticky=W, padx=120)

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_back.place(x=3, y=220)

        algorithm_label = Label(self, text="Algorithm fo study:", pady=3)
        algorithm_label.grid(row=4, column=0, sticky=W)

        rf = Radiobutton(self, text="Random Forest", variable=self.algorithm, value=1, command=self.enable_button)
        lr = Radiobutton(self, text="Logical regression", variable=self.algorithm, value=2, command=self.enable_button)
        rf.grid(row=5, column=0, sticky=W)
        lr.grid(row=6, column=0, sticky=W)

    def enable_button(self):
        if self.algorithm.get() >= 1:
            self.btn_submit['state'] = NORMAL

    def open_param_window(self):
        if not self.fail_col_name.get().strip():
            messagebox.showerror(title="Error", message="Column must not be empty")
        try:
            var = pd.read_file(self.file)[self.fail_col_name.get()]
            integer = int(self.count_data.get())
            if not self.is_int(integer):
                raise Exception("Count must be an positive integer")
            if integer > 6 or integer == 0:
                messagebox.showerror(title="Error", message="Count must be less than 7")
            elif not self.fail_col_name.get().strip():
                messagebox.showerror(title="Error", message="Column must not be empty")
            flag = pd.check_value_col(pd.read_file(self.file), self.fail_col_name.get())
            if flag is None:
                raise Exception("Values for Failure column must be 0/1 (No/Yes)")
            ppw.ParamPredictionWindow(self, self.file, self.algorithm.get(), self.count_data.get(),
                                      self.fail_col_name.get())
            self.withdraw()
        except KeyError:
            messagebox.showerror(title="Error", message="Please enter correct name of column")
        except ValueError:
            messagebox.showerror(title="Error", message="Count must be an positive integer")
        except Exception as e:
            messagebox.showerror(title="Error", message=e)

    def is_int(self, value):
        try:
            var = float(value)
            if var.is_integer():
                if var <= 0:
                    return False
                else:
                    return True
        except ValueError:
            return False

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
