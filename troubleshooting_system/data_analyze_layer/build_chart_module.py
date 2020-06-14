import data_analyze_layer.analyze_module as adm
import data_analyze_layer.data_processing_module as dpm
import matplotlib.pyplot as plt
import numpy as np


def build_chart(param_col, param_fail, param_id, param, file):
    if param == 5:
        try:
            adm.build_pivot_chart(param_col, param_fail, dpm.read_file(file), param_id)
        except KeyError:
            return False
    if param == 1:
        try:
            adm.build_error_diagram(dpm.read_file(file), param_fail)
        except KeyError:
            return False
    if param == 2:
        try:
            adm.build_dependency_diagram(param_col, param_fail, dpm.read_file(file))
        except KeyError:
            return False
    if param == 3:
        try:
            adm.build_histogram(dpm.read_file(file), param_col)
        except KeyError:
            return False
    if param == 4:
        try:
            adm.build_boxplot(dpm.read_file(file), param_col)
        except KeyError:
            return False
    return True


def get_colors(count):
    colors = []
    cm = plt.cm.get_cmap('hsv', count)
    for i in np.arange(count):
        colors.append(cm(i))
    return colors
