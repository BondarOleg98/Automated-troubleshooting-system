import os
import tkinter
import troubleshooting_system.functions.analyze_data as ad
from tkinter import *
from tkinter import messagebox
from pandastable import Table
import troubleshooting_system.windows.chart_window as cw


class AnalyzeWindow(tkinter.Toplevel):
    def __init__(self, root, file):
        super().__init__(root)
        self.root = root
        self.param = IntVar()
        self.file = file
        self.flag_id = StringVar()
        self.flag_id.set(DISABLED)
        self.flag_col = StringVar()
        self.flag_col.set(DISABLED)
        self.flag_fail = StringVar()
        self.flag_fail.set(DISABLED)
        self.flag_btn = StringVar()
        self.flag_btn.set(DISABLED)
        self.col_name = StringVar()
        self.fail_col_name = StringVar()
        self.col_id_name = StringVar()
        self.init_analyze_window(file)
        self.param_col_entry = Entry(self, textvariable=self.col_name, state=self.flag_col.get())
        self.param_fail_entry = Entry(self, textvariable=self.fail_col_name, state=self.flag_fail.get())
        self.param_id_entry = Entry(self, textvariable=self.col_id_name, state=self.flag_id.get())
        self.btn_submit = tkinter.Button(self, text="Submit", anchor=SW, padx=10, command=self.open_window_chart
                                         , state=self.flag_btn.get())
        self.btn_submit.place(x=500, y=520)
        self.param_col_entry.grid(row=3, column=0, sticky=W, padx=442)
        self.param_fail_entry.grid(row=4, column=0, sticky=W, padx=442)
        self.param_id_entry.grid(row=5, column=0, sticky=W, padx=442)

        Label(self, text="Column name:").grid(row=3, column=0, sticky=W, padx=340)
        Label(self, text="Failure column name:").grid(row=4, column=0, sticky=W, padx=303)
        Label(self, text="Id column name:").grid(row=5, column=0, sticky=W, padx=328)
        self.protocol("WM_DELETE_WINDOW", self.exit_window)

    def init_analyze_window(self, file):
        self.title("Analyze window")
        self.geometry("570x550+300+80")
        # self.resizable(False, False)
        self.param.set(0)

        frame = tkinter.Frame(self)
        pt = Table(frame, dataframe=ad.find_statistics_param(file), height=176)
        pt.show()

        file = os.path.splitext(os.path.basename(file))[0]
        file_label = Label(self, text="Name file: " + file, font="Arial 18", pady=15, padx=210)
        file_label.grid(row=0, column=0, sticky=W)

        # frame.grid(fill='both')
        frame.grid(row=1, column=0, sticky=W)

        btn_back = tkinter.Button(self, text="Back", command=self.exit_window, anchor=SW, padx=10)
        btn_back.place(x=3, y=520)

        chart_label = Label(self, text="Choose diagram(chart):", font="Arial 12", pady=15)
        chart_label.grid(row=2, column=0, sticky=W)

        param_label = Label(self, text="Enter parameters:", font="Arial 12", pady=15)
        param_label.grid(row=2, column=0, sticky=W, padx=430)

        pivot_chart = Radiobutton(self, text="Pivot chart", variable=self.param, value=5, command=self.choose_chart)
        err_diagram = Radiobutton(self, text="Error diagram", variable=self.param, value=1, command=self.choose_chart)
        depend_diagram = Radiobutton(self, text="Dependency diagram", variable=self.param,
                                     value=2, command=self.choose_chart)
        histogram = Radiobutton(self, text="Histogram", variable=self.param, value=3, command=self.choose_chart)
        box_plot = Radiobutton(self, text="Box plot", variable=self.param, value=4, command=self.choose_chart)

        err_diagram.grid(row=3, column=0, sticky=W)
        depend_diagram.grid(row=4, column=0, sticky=W)
        histogram.grid(row=5, column=0, sticky=W)
        box_plot.grid(row=6, column=0, sticky=W)
        pivot_chart.grid(row=7, column=0, sticky=W)

    def choose_chart(self):
        if self.param.get() == 2:
            self.flag_fail.set(NORMAL)
            self.param_fail_entry['state'] = self.flag_fail.get()
            self.flag_col.set(NORMAL)
            self.param_col_entry['state'] = self.flag_col.get()
            self.flag_id.set(DISABLED)
            self.param_id_entry['state'] = self.flag_id.get()
            self.btn_submit['state'] = NORMAL
        elif self.param.get() == 1:
            self.flag_fail.set(NORMAL)
            self.param_fail_entry['state'] = self.flag_fail.get()
            self.flag_col.set(DISABLED)
            self.param_col_entry['state'] = self.flag_col.get()
            self.btn_submit['state'] = NORMAL
        elif self.param.get() == 5:
            self.flag_fail.set(NORMAL)
            self.param_fail_entry['state'] = self.flag_fail.get()
            self.flag_col.set(NORMAL)
            self.param_col_entry['state'] = self.flag_col.get()
            self.flag_id.set(NORMAL)
            self.param_id_entry['state'] = self.flag_id.get()
            self.btn_submit['state'] = NORMAL
        else:
            self.flag_fail.set(DISABLED)
            self.param_fail_entry['state'] = self.flag_fail.get()
            self.flag_col.set(NORMAL)
            self.param_col_entry['state'] = self.flag_col.get()
            self.flag_id.set(DISABLED)
            self.param_id_entry['state'] = self.flag_id.get()
            self.btn_submit['state'] = NORMAL

    def open_window_chart(self):
        if self.check_entered_param(self.param_col_entry.get(), self.param_fail_entry.get(),
                                    self.param_id_entry.get(), self.param.get()):
            if not cw.build_chart(self.param_col_entry.get(), self.param_fail_entry.get(), self.param_id_entry.get(),
                                  self.param.get(), self.file):
                messagebox.showerror(title="Error", message="Please enter correct parameters")
        else:
            messagebox.showerror(title="Error", message="Please enter parameters")

    def check_entered_param(self, param_col, param_fail, param_id, param):
        if param == 1:
            if not param_fail.strip():
                return False
        elif param == 2:
            if not param_fail.strip() or not param_col.strip():
                return False
        elif param == 5:
            if not param_fail.strip() or not param_col.strip() or not param_id.strip():
                return False
        else:
            if not param_col.strip():
                return False
        return True

    def exit_window(self):
        self.destroy()
        self.root.deiconify()
