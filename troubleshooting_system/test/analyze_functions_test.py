import unittest
import troubleshooting_system.functions.analyze_data as ad
import pandas as pd
import troubleshooting_system.windows.chart_window as cw


class MyTestCase(unittest.TestCase):
    path = "E:\\Project\\Automated-troubleshooting-system\\troubleshooting_system\\data\\test_data.csv"

    def test_on_correct_return_data(self):
        self.assertIsNotNone(ad.read_file(self.path), "Input data is None")
        self.assertTrue(type(ad.read_file(self.path)) == type(pd.DataFrame()))
        self.assertTrue(type(ad.find_statistics_param(self.path)), type(pd.DataFrame()))
        lst_return = ad.data_error('Temperature', 'Failure', ad.read_file(self.path))
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
