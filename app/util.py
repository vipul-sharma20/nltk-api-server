from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer


class NLTKStem(object):

    dispatch = {
        'porter': PorterStemmer,
        'snowball': SnowballStemmer
        }

    def __init__(self, options):
        self.options = options

    def stem(self):
        stemmer = self.dispatch['porter']
        if self.options.get('stemmer'):
            stemmer = self.dispatch[self.options['stemmer']]
        result = stemmer().stem(self.options.get('word'))
        return result

