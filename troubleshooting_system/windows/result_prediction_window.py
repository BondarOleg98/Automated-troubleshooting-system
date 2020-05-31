import tkinter
from tkinter import *
import troubleshooting_system.functions.prediction_data as pd


class ResultPredictionWindow(tkinter.Toplevel):
    def __init__(self, root, data, params, fail_col_name, algorithm):
        super().__init__(root)
        self.var = IntVar()
        self.root = root
        self.data = data
        self.params = []
        self.params = params
        self.fail_col_name = fail_col_name
        self.algorithm = algorithm
        self.init_result_window()
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_result_window(self):
        self.title("Result prediction window")
        self.geometry("400x240+300+200")
        self.focus_get()
        self.resizable(False, False)
        self.var.set(0)

        result_label = Label(self, text="Result prediction", font="Arial 15", pady=15, padx=120)
        result_label.grid(row=0, column=0, sticky=W)

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_back.place(x=3, y=210)

        success_label = Label(text="\nResult was written\nin file prediction_data_<algorithm>.csv")
        text = Text(self, width=400, height=8)
        text.insert(1.0, pd.prediction(self.data, self.params, self.fail_col_name, self.algorithm))
        text.tag_config('info', foreground="green")
        text.insert(END,success_label['text'], 'info')
        text.grid(row=1, column=0, sticky=W)

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
