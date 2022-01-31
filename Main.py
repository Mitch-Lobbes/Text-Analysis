import pandas as pd
from validate_email import validate_email


class TextAnalyser:

    def __init__(self, file):
        self._df = self._read_input(input_file=file)
        pd.set_option('display.max_rows', 400)

    @staticmethod
    def _read_input(input_file):
        return pd.read_csv(input_file, sep=';', encoding='ISO-8859-1')

    def run(self):
        self._df['is_valid_email'] = self._df['LOGIN'].apply(lambda x: validate_email(x))
        print(self._df)


filename = "text.csv"
analysis = TextAnalyser(file=filename)
analysis.run()
