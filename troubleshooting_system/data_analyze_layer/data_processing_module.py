import pandas as pd

from troubleshooting_system.data_analyze_layer.validation_module import check_value_col


def read_file_prediction(file):
    data = pd.read_csv(file, index_col=0)
    for col in data.columns:
        if data[col].dtype == object:
            continue
        median = data[col].median()
        data[col].fillna(median, inplace=True)
    return data


def read_file(file):
    data = pd.read_csv(file)
    return data


def dictionary_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    for key, value in my_dict:
        keys.append(key)
        values.append(value)
    return keys, values


def replace_value_data(data, lst_param, fail_param):
    try:
        if check_value_col(data, fail_param) is None:
            raise Exception()
        expected_output = check_value_col(data, fail_param)
        data_inputs = data[lst_param]
        return expected_output, data_inputs
    except KeyError:
        return None
    except Exception:
        return None


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
