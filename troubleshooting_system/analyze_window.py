import os
import tkinter
from tkinter import *


class AnalyzeWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.var = IntVar()
        self.file = os.path.splitext(os.path.basename(file))[0]
        self.init_child(self.file)

    def init_child(self, file):
        self.title("Analyze window")
        self.geometry("650x550+300+80")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.var.set(0)

        file_label = Label(self, text="Name file: "+file, font="Arial 18", pady=15)
        file_label.pack()

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_submit = tkinter.Button(self, text="Submit", anchor=SW, padx=10)
        btn_submit.place(x=580, y=520)
        btn_back.place(x=3, y=520)

        # analyze = Radiobutton(self, text="Analyze data", variable=self.var, value=0)
        # predict = Radiobutton(self, text="Prediction data", variable=self.var, value=1)
        # analyze.pack()
        # predict.pack()


    # def choose_function(self):
    #
    #

    def exit_window(self):
        self.destroy()