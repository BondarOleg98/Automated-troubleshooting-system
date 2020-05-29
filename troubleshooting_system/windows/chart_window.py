import tkinter
from tkinter import *
from turtle import pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import troubleshooting_system.functions.analyze_data as ad


class ChartWindow(tkinter.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_chart_window(self):
        self.title("Chart window")
        self.geometry("650x550+300+80")
        self.resizable(False, False)
        # f = Figure(figsize=(5, 5), dpi=100)
        # a = f.add_subplot(111)
        # a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
        #
        # canvas = FigureCanvasTkAgg(f, self)
        # canvas.show()
        # canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)
        #
        # # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # # toolbar.update()
        # canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
