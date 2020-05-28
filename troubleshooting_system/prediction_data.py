import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
from sklearn.ensemble import RandomForestClassifier

pd.options.mode.chained_assignment = None

FILE_PATH = 'machine.csv'

data = pd.read_csv(FILE_PATH)
data.Date = data.Date.apply(pd.to_datetime)
data_describe = data


def replace_value_data(data):
    data_inputs = data[
        ['Temperature', 'Humidity', 'Hours Since Previous Failure', 'Date.year', 'Date.month', 'Date.day-of-month',
         'Date.day-of-week']]
    expected_output = data['Failure']
    expected_output = np.where(expected_output == "No", 0, 1)
    return expected_output, data_inputs


def prediction(data):
    changed_data = replace_value_data(data)
    inputs_train, inputs_test, expected_output_train, expected_output_test = train_test_split(changed_data[1],
                                                                                              changed_data[0],
                                                                                              test_size=0.33,
                                                                                              random_state=42)
    dataPrediction(inputs_train, inputs_test, expected_output_train, expected_output_test, changed_data[1])


def dataPrediction(inputs_train, inputs_test, expected_output_train, expected_output_test, data_inputs):
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(inputs_train, expected_output_train)
    joblib.dump(rf, "mechanizm_model", compress=9)

    lr = LogisticRegression(max_iter=8000)
    lr.fit(inputs_train, expected_output_train)
    predicted_classes = lr.predict(inputs_test)
    # predicted_classes
    predictions = pd.Series(predicted_classes)
    parameters = lr.coef_

    pred = rf.predict(data_inputs)
    outPredictData(pred, parameters, data_inputs)
    # accuracyErrorPrediction(inputs_train, inputs_test, expected_output_test, predicted_classes, rf, lr)


def outPredictData(pred, parameters, data_inputs):
    count_no = 0
    count_yes = 0
    dictionary = {}
    my_list = []
    data_inputs['Pred failure'] = pred

    data_inputs.to_csv('prediction_data.csv')

    for element in pred:
        if element == 1:
            count_no += 1
        else:
            count_yes += 1
    print("No: " + str(count_yes) + " " + "Yes: " + str(count_no))
    print("Total: " + (str)(count_no + count_yes))
    print("#######################################")
    print(parameters)
    print("#######################################")
    for row in data_inputs.iterrows():
        if row[1]['Pred failure'] == 1:
            dictionary['Failure'] = 1
            dictionary['Temperature'] = row[1]['Temperature']
            dictionary['Humidity'] = row[1]['Humidity']
            my_list.append(dictionary)

    for element in my_list:
        print(element)
    print(len(my_list))


def loadPredictionModel(name_model):
    return joblib.load(name_model)


data = pd.read_csv(FILE_PATH, index_col=0)
prediction(data)
