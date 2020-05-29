import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.mode.chained_assignment = None


class AnalyzeData:
    def __init__(self):
        self.PLOT_LABEL_FONT_SIZE = 14

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

    def get_colors(self, count):
        colors = []
        cm = plt.cm.get_cmap('hsv', count)
        for i in np.arange(count):
            colors.append(cm(i))
        return colors

    def dictionary_sort(self, my_dict):
        keys = []
        values = []
        my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        for key, value in my_dict:
            keys.append(key)
            values.append(value)
        return keys, values

    def build_error_diagram(self, data, failure):
        failure_count = pd.value_counts(data[failure].values, sort=True)
        failure_count_keys, failure_count_values = self.dictionary_sort(dict(failure_count))
        failures = len(failure_count_keys)

        plt.title(failure + ' ', fontsize=data.PLOT_LABEL_FONT_SIZE)
        plt.bar(np.arange(failures), failure_count_values, color=self.get_colors(failures))
        plt.xticks(np.arange(failures), failure_count_keys, rotation=0, fontsize=12)
        plt.yticks(fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.ylabel('Count of failures', fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.show()

        print("No: " + str(failure_count['No']) + ' ' + "Yes: " + str(failure_count['Yes']))
        print("Total: " + str(failure_count['No'] + failure_count['Yes']))

    def data_error(self, name_column, data):
        array = []
        count_array = []
        data_set = set()
        for row in data.iterrows():
            if row[1]['Failure'] == 'Yes':
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

    def build_dependency_diagram(self, name_column):
        diagram_param = self.data_error(name_column)
        plt.xlabel(name_column, fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.ylabel('Count of failures', fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.bar(np.arange(diagram_param[0]), diagram_param[1], color=self.get_colors(diagram_param[0]))
        plt.xticks(np.arange(diagram_param[0]), diagram_param[2], rotation=0, fontsize=12)
        plt.yticks(fontsize=self.PLOT_LABEL_FONT_SIZE)
        name_column = name_column.lower()
        plt.title('Dependency between failure and ' + name_column, fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.show()

        plt.plot(diagram_param[2], diagram_param[1])
        plt.show()

    def build_histogram(self, data):
        plt.figure(figsize=(9, 8))
        sns.distplot(data['Temperature'], color='g', bins=100, hist_kws={'alpha': 0.4})
        plt.figure(figsize=(9, 8))
        sns.distplot(data['Humidity'], color='g', bins=100, hist_kws={'alpha': 0.4})

    def build_boxplot(self, data):
        sns.boxplot(x=data['Measure1'])
        sns.boxplot(x=data['Measure2'])
        sns.boxplot(x=data['Measure3'])
        data['Humidity'][data['Humidity'] < 70] = 70
        data['Humidity'][data['Humidity'] > 95] = 95
        sns.boxplot(x=data['Humidity'])
        data['Temperature'][data['Temperature'] < 60] = 60
        data['Temperature'][data['Temperature'] > 71.875] = 71.875
        sns.boxplot(x=data['Temperature'])

    def find_value_error(self, column1, column2, data):
        array_param_first = []
        array_param_second = []

        for row in data.iterrows():
            if row[1]['Failure'] == 'Yes':
                array_param_first.append(row[1][column1])
                array_param_second.append(row[1][column2])

        new_data = {column1: array_param_first, column2: array_param_second}
        df = pd.DataFrame(new_data, columns=[column1, column2])
        print('#########################################')
        print(df.mode())

    # data.info()
    # print('##############################################################')
    # print("NaN values:")
    # data.isnull().values.any()
    #
    # data.head(7905)
