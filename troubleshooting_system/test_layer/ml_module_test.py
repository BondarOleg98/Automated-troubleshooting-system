import math
import os
import unittest
from pathlib import Path

import troubleshooting_system.data_science_layer.ml_module as pd
import pandas as pnd


class TestPredictionFunctionCase(unittest.TestCase):
    path = "/troubleshooting_system/data_layer\\test_data.csv"

    def test_read_file_on_correct_return(self):
        self.assertIsNotNone(pd.read_file(self.path), "Input data_layer is None")
        self.assertTrue(type(pd.read_file(self.path)) == type(pnd.DataFrame()))

    def test_read_file_on_fill_empty(self):
        count_input_data = 0
        count_output_data = 0
        for el in pnd.read_csv(self.path)['Hours Since Previous Failure']:
            nan = float(el)
            if math.isnan(nan):
                count_input_data += 1
        for el in pd.read_file(self.path)['Hours Since Previous Failure']:
            nan = float(el)
            if math.isnan(nan):
                count_output_data += 1
        self.assertNotEqual(count_input_data, count_output_data)

    def test_correct_fill_median(self):
        current_val = pnd.read_csv(self.path)['Hours Since Previous Failure'].median()
        expected_val = pd.read_file(self.path)['Hours Since Previous Failure'][1]
        self.assertEqual(current_val, expected_val)

    def test_replace_value_data_correct_result(self):
        result_array = pd.replace_value_data(pnd.read_csv(self.path, index_col=0), ['Temperature', 'Humidity'],
                                             "Failure")
        self.assertEqual(len(result_array), 2)

    def test_replace_value_data_incorrect_input_data(self):
        check_none = pd.replace_value_data(pnd.read_csv(self.path), ['Temperature', 'Error'], "Failure")
        self.assertIsNone(check_none)
        check_none = pd.replace_value_data(pnd.read_csv(self.path), ['Temperature'], "Incorrect value")
        self.assertIsNone(check_none)

    def test_prediction_return_type(self):
        check_none = pd.prediction(pnd.read_csv(self.path), ['Temperature', 'Error'], "Failure", 1)
        self.assertIsNone(check_none)
        check_none = pd.prediction(pnd.read_csv(self.path), ['Temperature'], "Failure", 2)
        self.assertIsNotNone(check_none)
        self.assertEqual(type(check_none), str)

    def test_out_predict_data_save_file(self):
        home = str(Path.home())
        pd.prediction(pnd.read_csv(self.path), ['Temperature'], "Failure", 1)
        pd.prediction(pnd.read_csv(self.path), ['Temperature'], "Failure", 2)
        self.assertTrue(os.path.exists(home + "\\prediction_data_lr.csv"))
        self.assertTrue(os.path.exists(home + "\\prediction_data_rf.csv"))

    def test_save_model_file(self):
        home = str(Path.home())
        count_file_after = 0
        list_dir = os.listdir(home)
        for file in list_dir:
            if file.endswith('.pkl'):
                os.remove(home + "\\" + file)
        pd.prediction(pnd.read_csv(self.path), ['Temperature'], "Failure", 1)
        for file in list_dir:
            if file.endswith('.pkl'):
                count_file_after += 1
        self.assertTrue(count_file_after > 0)


if __name__ == '__main__':
    unittest.main()
