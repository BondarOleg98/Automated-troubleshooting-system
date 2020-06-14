import uuid
import joblib
from pathlib import Path


def out_predict_data(predicted, data_inputs, flag, algorithm):
    count_no = 0
    count_yes = 0
    data_inputs['Predicted failure'] = predicted
    home = str(Path.home())
    if flag == 'l':
        data_inputs.to_csv(home + "\\prediction_data_lr.csv")
        joblib.dump(algorithm, str(Path.home()) + "\\prediction_data_lr_" + str(uuid.uuid4()) + ".pkl", compress=9)
    else:
        data_inputs.to_csv(home + "\\prediction_data_rf.csv")
        joblib.dump(algorithm, str(Path.home()) + "\\prediction_data_rf_" + str(uuid.uuid4()) + ".pkl", compress=9)
    for element in predicted:
        if element == 1:
            count_yes += 1
        else:
            count_no += 1
    return "No error: " + str(count_no) + " " + "Yes error: " + str(count_yes) + "\n" + \
           "Total: " + str(count_no + count_yes)