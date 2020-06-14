import unittest
import data_analyze_layer.analyze_module as ad
import data_analyze_layer.data_processing_module as dpm
import pandas as pd


class TestDataAnalyzeCase(unittest.TestCase):
    path = "E:\\Project\\Automated-troubleshooting-system\\troubleshooting_system\\data_layer\\test_data.csv"

    def test_on_correct_return_data(self):
        self.assertIsNotNone(dpm.read_file(self.path), "Input data_layer is None")
        self.assertTrue(type(dpm.read_file(self.path)) == type(pd.DataFrame()))
        self.assertTrue(type(ad.find_statistics_param(self.path)), type(pd.DataFrame()))
        lst_return = ad.data_error('Temperature', 'Failure', dpm.read_file(self.path))
        self.assertTrue(len(lst_return) == 3)
        self.assertEqual(type(lst_return[0]), int)
        self.assertEqual(type(lst_return[1]), list)
        self.assertEqual(type(lst_return[2]), list)
        self.assertTrue(len(ad.get_colors(7)) == 7)
        self.assertEqual(type(ad.get_colors(7)), list)
        output_data = ad.dictionary_sort({"param1": 1, "param2": 2})
        self.assertTrue(len(output_data) == 2)


if __name__ == '__main__':
    unittest.main()
