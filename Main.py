import pandas as pd
import nltk
from validate_email import validate_email
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
pd.set_option('display.max_rows', 400)

class TextAnalyser:

    def __init__(self, file):
        self._df = self._read_input(input_file=file)
        self._list = []


    @staticmethod
    def _read_input(input_file):
        return pd.read_csv(input_file, sep=';', encoding='ISO-8859-1')

    def run(self):
        self._df['is_valid_email'] = self._df['LOGIN'].apply(lambda x: validate_email(x))
        self._df['tokenized words'] = self._df['V2'].apply(lambda x: word_tokenize(str(x)))

        for i in self._df['tokenized words']:
            self._list.extend(i)

        distribution = FreqDist(self._list)
        print(distribution.most_common())

        stop_words = set(stopwords.words("dutch"))
        print(stop_words)

filename = "text.csv"
analysis = TextAnalyser(file=filename)
analysis.run()
