from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer


class NLTKStem(object):
    """
    NLTK Stemmers used: Porter, Snowball and Lancaster
    """

    dispatch = {
        'porter': PorterStemmer,
        'snowball': SnowballStemmer,
        'lancaster': LancasterStemmer,
        }

    def __init__(self, options):
        self.options = options

    def stem(self):
        stemmer = self.options.get('stemmer', 'snowball')
        stemmer_obj = self.dispatch[stemmer]

        if stemmer == 'snowball':
            ignore_stopwords = False

            if self.options.get('ignore_stopwords'):
                if self.options['ignore_stopwords'] == 'true':
                    ignore_stopwords = True
            language = self.options.get('language', 'english')

            result = stemmer_obj(language, ignore_stopwords).stem(self.options['word'])

        else:
            result = stemmer_obj().stem(self.options['word'])

        return self._dump(result)

    def _dump(self, result):
        response = {
                'status': True,
                'result': result
                }
        return response

