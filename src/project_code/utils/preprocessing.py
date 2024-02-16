import re
import string
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk


class PreprocessingUtils:
    def __init__(self):
        try:
            self.stop_words = set(stopwords.words("english"))
        except LookupError:
            nltk.download("stopwords")
            self.stop_words = set(stopwords.words("english"))
        if "stemmer" not in globals():
            self.stemmer = SnowballStemmer("english")

    # Limpieza de texto
    def clean_text(self, text):
        text = str(text).lower()
        text = re.sub("\[.*?\]", "", text)
        text = re.sub("https?://\S+|www\.\S+", "", text)
        text = re.sub("<.*?>+", "", text)
        text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
        text = re.sub("\n", "", text)
        text = re.sub("\w*\d\w*", "", text)
        return text

    def preprocess_data(self, text):
        text = self.clean_text(text)
        text = " ".join(word for word in text.split() if word not in self.stop_words)
        text = " ".join(self.stemmer.stem(word) for word in text.split())
        return text
