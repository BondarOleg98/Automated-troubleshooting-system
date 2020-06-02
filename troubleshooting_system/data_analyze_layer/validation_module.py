import math
import numpy as np


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
                raise Exception
            expected_output = np.where(expected_output == "No", 0, 1)
            data[fail_param] = expected_output
            median = data[fail_param].median()
            data[fail_param].fillna(median, inplace=True)
            expected_output = data[fail_param]
        return expected_output
    except Exception:
        return None