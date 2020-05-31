import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import joblib
pd.options.mode.chained_assignment = None


def replace_value_data(data, lst_param, fail_param):
    data_inputs = data[lst_param]
    expected_output = data[fail_param]
    expected_output = np.where(expected_output == "No", 0, 1)  ####!!!!!!!!!!!!!!!!
    return expected_output, data_inputs


def prediction(data, lst_param, fail_param, algorithm):
    # replace_value_data(data, lst_param, fail_param)
    changed_data = replace_value_data(data, lst_param, fail_param)
    inputs_train, inputs_test, expected_output_train, expected_output_test = train_test_split(changed_data[1],
                                                                                              changed_data[0],
                                                                                              test_size=0.33,
                                                                                              random_state=42)
    if algorithm == 1:
        data_prediction_rf(inputs_train, inputs_test, expected_output_train, expected_output_test, changed_data[1])
    else:
        data_prediction_lr(inputs_train, inputs_test, expected_output_train, expected_output_test, changed_data[1])


def data_prediction_rf(inputs_train, inputs_test, expected_output_train, expected_output_test, data_inputs):
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(inputs_train, expected_output_train)
    # joblib.dump(rf, "E:\\Project\\Automated-troubleshooting-system\\troubleshooting_system\\data", compress=9)
    predicted = rf.predict(data_inputs)
    predict_for_test = rf.predict(inputs_test)
    accuracy_error_prediction(inputs_test, expected_output_test, predict_for_test, rf)
    out_predict_data(predicted, data_inputs, 'r')


def data_prediction_lr(inputs_train, inputs_test, expected_output_train, expected_output_test, data_inputs):
    lr = LogisticRegression(max_iter=8000)
    lr.fit(inputs_train, expected_output_train)
    predicted = lr.predict(data_inputs)
    # joblib.dump(lr, "E:\\Project\\Automated-troubleshooting-system\\troubleshooting_system\\data", compress=9)
    predict_for_test = lr.predict(inputs_test)
    accuracy_error_prediction(inputs_test, expected_output_test, predict_for_test, lr)
    out_predict_data(predicted, data_inputs, 'l')


def out_predict_data(predicted, data_inputs, flag):
    count_no = 0
    count_yes = 0
    data_inputs['Predicted failure'] = predicted
    if flag == 'l':
        data_inputs.to_csv('prediction_data_lr.csv')
    else:
        data_inputs.to_csv('prediction_data_rf.csv')
    for element in predicted:
        if element == 1:
            print("Error")
            count_yes += 1
        else:
            count_no += 1
    print("No: " + str(count_no) + " " + "Yes: " + str(count_yes))
    print("Total: " + (str)(count_no + count_yes))


def load_prediction_model(name_model):
    return joblib.load(name_model)


def accuracy_error_prediction(inputs_test, expected_output_test, predicted, algorithm):
    accuracy = algorithm.score(inputs_test, expected_output_test)
    print("Accuracy = {}%".format(accuracy * 100))
    print('MAE:', metrics.mean_absolute_error(expected_output_test, predicted))
    print('MSE:', metrics.mean_squared_error(expected_output_test, predicted))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(expected_output_test, predicted)))


def read_file(file):
    data = pd.read_csv(file, index_col=0)
    data.Date = data.Date.apply(pd.to_datetime)
    return data

# data.isnull().values.any()
