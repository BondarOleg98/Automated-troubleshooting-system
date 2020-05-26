import tkinter
from tkinter import *
import analyze_window as aw
import prediction_window as pw


class FunctionWindow(tkinter.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.var = IntVar()
        self.init_child()

    def init_child(self):
        self.title("Function window")
        self.geometry("300x300+300+200")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.var.set(0)

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_submit = tkinter.Button(self, text="Submit", command=self.choose_function, anchor=SW, padx=10)
        btn_submit.place(x=230, y=270)
        btn_back.place(x=3, y=270)

        analyze = Radiobutton(self, text="Analyze data", variable=self.var, value=0)
        predict = Radiobutton(self, text="Prediction data", variable=self.var, value=1)
        analyze.pack()
        predict.pack()

    def choose_function(self):

        if self.var.get() == 0:
            aw.AnalyzeWindow(self)
        elif self.var.get() == 1:
            pw.PredictionWindow(self)

    def exit_window(self):
        self.destroy()
