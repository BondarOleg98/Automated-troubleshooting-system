from sklearn import metrics
import numpy as np


def accuracy_error_prediction(inputs_test, expected_output_test, predicted, algorithm):
    accuracy = algorithm.score(inputs_test, expected_output_test)
    return "Accuracy = {}%".format(accuracy * 100) + "\n" + \
           "MAE: " + str(metrics.mean_absolute_error(expected_output_test, predicted)) + "\n" \
                                                                                         "MSE: " + str(
        metrics.mean_squared_error(expected_output_test, predicted)) + "\n" + \
           "RMSE: " + str(np.sqrt(metrics.mean_squared_error(expected_output_test, predicted))) + "\n"