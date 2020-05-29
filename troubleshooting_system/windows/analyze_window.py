import os
import tkinter
import troubleshooting_system.functions.analyze_data as ad
from tkinter import *
from pandastable import Table
import troubleshooting_system.windows.param_analyze_window as paw


class AnalyzeWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.root = root
        self.param = IntVar()
        self.init_analyze_window(file)
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_analyze_window(self, file):
        self.title("Analyze window")
        self.geometry("650x550+300+80")
        self.resizable(False, False)
        self.param.set(0)

        frame = tkinter.Frame(self)
        # frame.pack(fill='both', expand=True)
        pt = Table(frame, dataframe=ad.AnalyzeData.find_statistics_param(file), height=176)
        pt.show()

        file = os.path.splitext(os.path.basename(file))[0]
        file_label = Label(self, text="Name file: " + file, font="Arial 18", pady=15)
        file_label.pack()

        frame.pack(fill='both')

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_submit = tkinter.Button(self, text="Submit", anchor=SW, padx=10, command=self.choose_chart)
        btn_submit.place(x=580, y=520)
        btn_back.place(x=3, y=520)

        file_label = Label(self, text="Choose diagram(chart)", font="Arial 12", pady=15)
        file_label.pack()

        err_diagram = Radiobutton(self, text="Error diagram", variable=self.param, value=1)
        depend_diagram = Radiobutton(self, text="Dependency diagram", variable=self.param, value=2)
        histogram = Radiobutton(self, text="Histogram", variable=self.param, value=3)
        boxplot = Radiobutton(self, text="Boxplot", variable=self.param, value=4)

        err_diagram.pack()
        depend_diagram.pack()
        histogram.pack()
        boxplot.pack()

    def choose_chart(self):
        paw.ParamAnalyzeWindow(self, self.param.get())

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
