import troubleshooting_system.functions.analyze_data as ad


class ChartWindow():
    def __init__(self, param_col_entry, param_fail_entry, param):
        self.param_col_entry = param_col_entry
        self.param_fail_entry = param_fail_entry
        self.param = param
        self.init_chart_window()

    def init_chart_window(self):
        print(self.param)
        if self.param == 1:
            ad.build_error_diagram(ad.AnalyzeData.read_file(
                'E:\\Project\\Automated-troubleshooting-system\\'
                'troubleshooting_system\\functions\\test.csv'), self.param_fail_entry)

