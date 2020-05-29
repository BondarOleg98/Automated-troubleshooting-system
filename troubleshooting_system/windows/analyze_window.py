import os
import tkinter
import troubleshooting_system.functions.analyze_data as ad
from tkinter import *
from pandastable import Table


class AnalyzeWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.var = IntVar()
        self.root = root
        self.init_analyze_window(file)
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_analyze_window(self, file):
        self.title("Analyze window")
        self.geometry("650x550+300+80")
        self.resizable(False, False)
        self.var.set(0)

        frame = tkinter.Frame(self)
        # frame.pack(fill='both', expand=True)
        pt = Table(frame, dataframe=ad.AnalyzeData.find_statistics_param(file), height=176)
        pt.show()

        file = os.path.splitext(os.path.basename(file))[0]
        file_label = Label(self, text="Name file: " + file, font="Arial 18", pady=15)
        file_label.pack()

        frame.pack(fill='both')

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_submit = tkinter.Button(self, text="Submit", anchor=SW, padx=10)
        btn_submit.place(x=580, y=520)
        btn_back.place(x=3, y=520)

        file_label = Label(self, text="Choose diagram(chart)", font="Arial 12", pady=15)
        file_label.pack()

        err_diagram = Radiobutton(self, text="Error diagram", variable=self.var, value=0)
        depend_diagram = Radiobutton(self, text="Dependency diagram", variable=self.var, value=1)
        histogram = Radiobutton(self, text="Histogram", variable=self.var, value=2)
        boxplot = Radiobutton(self, text="Boxplot", variable=self.var, value=3)

        err_diagram.pack()
        histogram.pack()
        boxplot.pack()
        depend_diagram.pack()

    def choose_function(self):
        if self.var.get() == 0:
            # aw.AnalyzeWindow(self, self.file)
            self.withdraw()
        elif self.var.get() == 1:
            # pw.PredictionWindow(self)
            self.withdraw()

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
