import re
import string
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk


class PreprocessingUtils:
    """
    A utility class for preprocessing textual data. This class includes methods
    for cleaning and preprocessing text data. It utilizes NLTK's stopwords
    and SnowballStemmer for English language.

    Attributes:
        stop_words (set): A set of stopwords for English language.
        stemmer (SnowballStemmer): An instance of SnowballStemmer for English language.
    """

    def __init__(self):
        """
        Initializes the PreprocessingUtils class. Loads the set of English stopwords
        from NLTK's corpus. If not available, it downloads them. Also, initializes
        the SnowballStemmer for English language.
        """
        try:
            self.stop_words = set(stopwords.words("english"))
        except LookupError:
            nltk.download("stopwords")
            self.stop_words = set(stopwords.words("english"))
        if "stemmer" not in globals():
            self.stemmer = SnowballStemmer("english")

    def clean_text(self, text):
        """
        Cleans a given text by performing a series of regex operations.

        Steps:
        1. Converts to lower case.
        2. Removes text within square brackets.
        3. Removes URLs.
        4. Removes HTML tags.
        5. Removes punctuation.
        6. Removes new lines.
        7. Removes words containing numbers.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        text = str(text).lower()
        text = re.sub("\[.*?\]", "", text)
        text = re.sub("https?://\S+|www\.\S+", "", text)
        text = re.sub("<.*?>+", "", text)
        text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
        text = re.sub("\n", "", text)
        text = re.sub("\w*\d\w*", "", text)
        return text

    def preprocess_data(self, text):
        """
        Preprocesses the given text by cleaning it and then removing stopwords and
        stemming the words.

        Args:
            text (str): The text to be preprocessed.

        Returns:
            str: The preprocessed text.
        """
        text = self.clean_text(text)
        text = " ".join(word for word in text.split() if word not in self.stop_words)
        text = " ".join(self.stemmer.stem(word) for word in text.split())
        return text
