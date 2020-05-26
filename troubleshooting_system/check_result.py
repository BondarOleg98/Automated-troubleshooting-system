import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
pd.options.mode.chained_assignment = None


def accuracyErrorPrediction(inputs_train, inputs_test, expected_output_test, predicted_classes, rf,lr):
    accuracy = rf.score(inputs_test, expected_output_test)
    print("Accuracy = {}%".format(accuracy * 100))
    accuracy = lr.score(inputs_test, expected_output_test)
    print("Accuracy = {}%".format(accuracy * 100))
    print('MAE:', metrics.mean_absolute_error(expected_output_test, predicted_classes))
    print('MSE:', metrics.mean_squared_error(expected_output_test, predicted_classes))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(expected_output_test, predicted_classes)))