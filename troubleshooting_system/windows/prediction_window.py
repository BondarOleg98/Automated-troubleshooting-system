import tkinter
from tkinter import *


class PredictionWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.var = IntVar()
        self.root = root
        self.file = file
        self.init_child()
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_child(self):
        self.title("Prediction window")
        self.geometry("300x300+300+200")
        self.resizable(False, False)
        # self.grab_set()
        # self.focus_set()
        self.var.set(0)

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_submit = tkinter.Button(self, text="Submit", anchor=SW, padx=10)
        btn_submit.place(x=230, y=270)
        btn_back.place(x=3, y=270)

        analyze = Radiobutton(self, text="Random Forest", variable=self.var, value=0)
        predict = Radiobutton(self, text="Logical regression", variable=self.var, value=1)
        analyze.pack()
        predict.pack()

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
