import troubleshooting_system.data_science_layer.analyze_module as ad


def build_chart(param_col, param_fail, param_id, param, file):
    if param == 5:
        try:
            ad.build_pivot_chart(param_col, param_fail, ad.read_file(file), param_id)
        except KeyError:
            return False
    if param == 1:
        try:
            ad.build_error_diagram(ad.read_file(file), param_fail)
        except KeyError:
            return False
    if param == 2:
        try:
            ad.build_dependency_diagram(param_col, param_fail, ad.read_file(file))
        except KeyError:
            return False
    if param == 3:
        try:
            ad.build_histogram(ad.read_file(file), param_col)
        except KeyError:
            return False
    if param == 4:
        try:
            ad.build_boxplot(ad.read_file(file), param_col)
        except KeyError:
            return False
    return True



