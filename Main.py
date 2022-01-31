import pandas as pd


class TextAnalyser:

    def __init__(self, file):
        self._file = self._read_input(input_file=file)

    @staticmethod
    def _read_input(input_file):
        return pd.read_csv(input_file, sep=';', encoding='ISO-8859-1')

    def run(self):
        print(self._file)


filename = "text.csv"
analysis = TextAnalyser(file=filename)
analysis.run()
