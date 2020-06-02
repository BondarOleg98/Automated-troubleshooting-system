import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from troubleshooting_system.data_analyze_layer.build_chart_module import get_colors
from troubleshooting_system.data_analyze_layer.data_processing_module import data_error, dictionary_sort

pd.options.mode.chained_assignment = None

PLOT_LABEL_FONT_SIZE = 14


def find_statistics_param(file):
    data = pd.read_csv(file)
    try:
        data.Date = data.Date.apply(pd.to_datetime)
        data = data.drop(['ID'], axis=1)
    except AttributeError:
        return data.describe()
    except KeyError:
        return data.describe()
    return data.describe()


def build_dependency_diagram(name_column, failure_column, data):
    sns.set()
    plt.close("Dependency diagram (line)")
    plt.close("Dependency diagram")

    diagram_param = data_error(name_column, failure_column, data)
    plt.figure("Dependency diagram")
    plt.xlabel(name_column, fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Count of failures', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(diagram_param[0]), diagram_param[1], color=get_colors(diagram_param[0]))
    plt.xticks(np.arange(diagram_param[0]), diagram_param[2], rotation=0, fontsize=12)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    name_column_diagram = name_column.lower()
    plt.title('Dependency between failure and ' + name_column_diagram, fontsize=PLOT_LABEL_FONT_SIZE)

    plt.figure("Dependency diagram (line)")
    plt.xlabel(name_column, fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Count of failures', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.title('Dependency between failure and ' + name_column_diagram, fontsize=PLOT_LABEL_FONT_SIZE)
    plt.plot(diagram_param[2], diagram_param[1])
    plt.show()


def build_pivot_chart(name_column, failure_column, data, id_col):
    sns.set()
    data.pivot_table(id_col, name_column, failure_column, 'count'). \
        plot(kind='bar', stacked=True,
             title="Pivot data_layer of " + name_column.lower() + " and " + failure_column.lower())
    plt.show()


def build_histogram(data, name_column):
    sns.set()
    plt.figure("Histogram")
    plt.title("Histogram " + name_column.lower())
    sns.distplot(data[name_column], color='g', bins=100, hist_kws={'alpha': 0.4})
    plt.show()


def build_boxplot(data, name_column):
    plt.figure("Box plot")
    plt.title("Box plot " + name_column.lower())
    sns.boxplot(x=data[name_column])
    plt.show()


def build_error_diagram(data, failure_column):
    sns.set()
    failure_count = pd.value_counts(data[failure_column].values, sort=True)
    failure_count_keys, failure_count_values = dictionary_sort(dict(failure_count))
    failures = len(failure_count_keys)
    plt.figure("Error chart")
    plt.title(failure_column + ' ', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(failures), failure_count_values)
    plt.xticks(np.arange(failures), failure_count_keys, rotation=0, fontsize=12)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Count of failures', fontsize=14)
    plt.show()
