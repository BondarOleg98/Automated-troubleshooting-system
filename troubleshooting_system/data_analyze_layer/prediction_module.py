import uuid
import joblib
import pandas as pd
from data_analyze_layer.accuracy_module import accuracy_error_prediction
from data_analyze_layer.data_processing_module import replace_value_data
from data_analyze_layer.save_module import out_predict_data
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path


pd.options.mode.chained_assignment = None


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
    predicted = rf.predict(data_inputs)
    predict_for_test = rf.predict(inputs_test)
    return str(accuracy_error_prediction(inputs_test, expected_output_test, predict_for_test, rf)) + \
           str(out_predict_data(predicted, data_inputs, 'r', rf))


def data_prediction_lr(inputs_train, inputs_test, expected_output_train, expected_output_test, data_inputs):
    lr = LogisticRegression(max_iter=8000)
    lr.fit(inputs_train, expected_output_train)
    predicted = lr.predict(data_inputs)
    home = str(Path.home())
    joblib.dump(lr, home + "\\prediction_data_lr_" + str(uuid.uuid4())+".pkl", compress=9)
    predict_for_test = lr.predict(inputs_test)
    return str(accuracy_error_prediction(inputs_test, expected_output_test, predict_for_test, lr)) + \
           str(out_predict_data(predicted, data_inputs, 'l', lr))




