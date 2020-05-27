import tkinter
from tkinter import *
import analyze_window as aw
import prediction_window as pw


class FunctionWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.var = IntVar()
        self.init_child()
        self.file = file

    def init_child(self):
        self.title("Function window")
        self.geometry("300x180+300+200")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.var.set(0)
        function_label = Label(self, text="Choose function", font="Arial 15", pady=15)
        function_label.pack()

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_submit = tkinter.Button(self, text="Submit", command=self.choose_function, anchor=SW, padx=10)
        btn_submit.place(x=230, y=150)
        btn_back.place(x=3, y=150)

        analyze = Radiobutton(self, text="Analyze data", variable=self.var, value=0)
        predict = Radiobutton(self, text="Prediction data", variable=self.var, value=1)
        analyze.pack()
        predict.pack()

    def choose_function(self):

        if self.var.get() == 0:
            aw.AnalyzeWindow(self, self.file)
        elif self.var.get() == 1:
            pw.PredictionWindow(self)

    def exit_window(self):
        self.destroy()
