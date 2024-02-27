import re
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
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

    def clean(self, text):
        text = text.lower()  # Converting to lowerCase
        text = re.sub(
            "[%s]" % re.escape(string.punctuation), " ", text
        )  # removing punctuation

        text_tokens = word_tokenize(text)  # removing stopwords
        tw = [word for word in text_tokens if not word in self.stop_words]
        text = (" ").join(tw)

        splt = text.split(" ")
        output = [x for x in splt if len(x) > 3]  # removing words with length<=3
        text = (" ").join(output)

        text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)  # removing single character
        text = re.sub("<.*?>+", " ", text)  # removing HTML Tags
        text = re.sub("\n", " ", text)  # removal of new line characters
        text = re.sub(r"\s+", " ", text)  # removal of multiple spaces
        return text

    def data_preprocessing(self, text):
        tokens = word_tokenize(text)  # Tokenization
        tokens = [
            WordNetLemmatizer().lemmatize(word) for word in tokens
        ]  # Lemmetization
        tokens = [
            SnowballStemmer(language="english").stem(word) for word in tokens
        ]  # Stemming
        return " ".join(tokens)
