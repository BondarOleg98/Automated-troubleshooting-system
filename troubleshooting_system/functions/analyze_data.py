import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.mode.chained_assignment = None

PLOT_LABEL_FONT_SIZE = 14


def read_file(file):
    data = pd.read_csv(file)
    return data


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


def data_error(name_column, failure_column, data):
    array = []
    count_array = []
    data_set = set()
    for row in data.iterrows():
        if row[1][failure_column] == 'Yes':
            array.append(row[1][name_column])
        if row[1][failure_column] == 1:
            array.append(row[1][name_column])
    array.sort()

    for element in array:
        data_set.add(element)
    data_set = sorted(data_set, key=None, reverse=False)

    for element_set in data_set:
        count_value = array.count(element_set)
        count_array.append(count_value)
    count_value = len(count_array)

    return count_value, count_array, data_set


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
    data.pivot_table(id_col, name_column, failure_column, 'count').\
        plot(kind='bar', stacked=True,
             title="Pivot data of " + name_column.lower()+ " and " + failure_column.lower())
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


def get_colors(count):
    colors = []
    cm = plt.cm.get_cmap('hsv', count)
    for i in np.arange(count):
        colors.append(cm(i))
    return colors


def dictionary_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    for key, value in my_dict:
        keys.append(key)
        values.append(value)
    return keys, values


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

