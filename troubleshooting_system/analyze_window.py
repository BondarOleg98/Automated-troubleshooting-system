import os
import tkinter
from tkinter import *
import pandas as pd
from pandastable import Table


class AnalyzeWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.var = IntVar()
        self.root = root
        self.init_child(file)
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_child(self, file):
        self.title("Analyze window")
        self.geometry("650x550+300+80")
        self.resizable(False, False)
        self.var.set(0)

        frame = tkinter.Frame(self)
        # frame.pack(fill='both', expand=True)
        data = pd.read_csv(file)
        data = data.drop(['ID'], axis=1)
        # data = data.describe()
        pt = Table(frame, dataframe=data, height=176)
        pt.show()

        file = os.path.splitext(os.path.basename(file))[0]
        file_label = Label(self, text="Name file: " + file, font="Arial 18", pady=15)
        file_label.pack()

        frame.pack(fill='both')

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
        self.root.deiconify()
