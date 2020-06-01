import uuid
from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import joblib
import math

pd.options.mode.chained_assignment = None


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


def check_value_col(data, fail_param):
    try:
        expected_output = data[fail_param]
        if data[fail_param].dtype == object:
            count_flag = 0
            count_nan = 0
            for el in expected_output:
                if el == "No" or el == "Yes":
                    count_flag += 1
                elif type(el) != str:
                    nan = float(el)
                    if math.isnan(nan):
                        count_nan += 1
            divider = expected_output.size - count_nan - count_flag
            if divider != 0:
                raise Exception()
            expected_output = np.where(expected_output == "No", 0, 1)
            data[fail_param] = expected_output
            median = data[fail_param].median()
            data[fail_param].fillna(median, inplace=True)
            expected_output = data[fail_param]
        return expected_output
    except Exception:
        return None


def prediction(data, lst_param, fail_param, algorithm):
    changed_data = replace_value_data(data, lst_param, fail_param)

    if changed_data is None:
        return None

    inputs_train, inputs_test, expected_output_train, expected_output_test = train_test_split(changed_data[1],
                                                                                              changed_data[0],
                                                                                              test_size=0.33,
                                                                                              random_state=42)
    if algorithm == 1:
        return data_prediction_rf(inputs_train, inputs_test, expected_output_train, expected_output_test,
                                  changed_data[1])
    else:
        return data_prediction_lr(inputs_train, inputs_test, expected_output_train, expected_output_test,
                                  changed_data[1])


def data_prediction_rf(inputs_train, inputs_test, expected_output_train, expected_output_test, data_inputs):
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(inputs_train, expected_output_train)
    home = str(Path.home())
    joblib.dump(rf, home + "\\prediction_data_rf_" + str(uuid.uuid4())+".pkl", compress=9)
    predicted = rf.predict(data_inputs)
    predict_for_test = rf.predict(inputs_test)
    return str(accuracy_error_prediction(inputs_test, expected_output_test, predict_for_test, rf)) + \
           str(out_predict_data(predicted, data_inputs, 'r'))


def data_prediction_lr(inputs_train, inputs_test, expected_output_train, expected_output_test, data_inputs):
    lr = LogisticRegression(max_iter=8000)
    lr.fit(inputs_train, expected_output_train)
    predicted = lr.predict(data_inputs)
    home = str(Path.home())
    joblib.dump(lr, home + "\\prediction_data_lr_" + str(uuid.uuid4())+".pkl", compress=9)
    predict_for_test = lr.predict(inputs_test)
    return str(accuracy_error_prediction(inputs_test, expected_output_test, predict_for_test, lr)) + \
           str(out_predict_data(predicted, data_inputs, 'l'))


def out_predict_data(predicted, data_inputs, flag):
    count_no = 0
    count_yes = 0
    data_inputs['Predicted failure'] = predicted
    home = str(Path.home())
    if flag == 'l':
        data_inputs.to_csv(home + "\\prediction_data_lr.csv")
    else:
        data_inputs.to_csv(home + "\\prediction_data_rf.csv")
    for element in predicted:
        if element == 1:
            count_yes += 1
        else:
            count_no += 1
    return "No error: " + str(count_no) + " " + "Yes error: " + str(count_yes) + "\n" + \
           "Total: " + str(count_no + count_yes)


def accuracy_error_prediction(inputs_test, expected_output_test, predicted, algorithm):
    accuracy = algorithm.score(inputs_test, expected_output_test)
    return "Accuracy = {}%".format(accuracy * 100) + "\n" + \
           "MAE: " + str(metrics.mean_absolute_error(expected_output_test, predicted)) + "\n" \
                                                                                         "MSE: " + str(
        metrics.mean_squared_error(expected_output_test, predicted)) + "\n" + \
           "RMSE: " + str(np.sqrt(metrics.mean_squared_error(expected_output_test, predicted))) + "\n"


def read_file(file):
    data = pd.read_csv(file, index_col=0)
    for col in data.columns:
        if data[col].dtype == object:
            continue
        median = data[col].median()
        data[col].fillna(median, inplace=True)
    return data
