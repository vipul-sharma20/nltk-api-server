from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer

from nltk import word_tokenize
from nltk.tokenize import TweetTokenizer, StanfordTokenizer
from nltk.tokenize.api import StringTokenizer

from app.constants import DEFAULT_STEMMER, DEFAULT_TOKENIZER

class NLTKStem(object):
    """
    NLTK Stemmers used: Porter, Snowball and Lancaster

    Accepts:

    /api/stem?word=<word>/
    /api/stem?word=<word>&stemmer=<porter/snowball/lancaster>/
    /api/stem?word=<word>&stemmer=snowball&language=<language>&ignore_stopwords=<true/false>/

    Query Parameters:

        * Mandatory:
            1. word:
                type: string
        * Optional:
            1. stemmer:
                value: porter/snowball/lancaster
                default: snowball
            2. ignore_stopwords: Only for Snowball Stemmer
                value: true/false
                default: false
            3. language: Only for Snowball Stemmer
                value: see SnowballStemmer.languages
                default: english
    """

    dispatch = {
        'porter': PorterStemmer,
        'snowball': SnowballStemmer,
        'lancaster': LancasterStemmer,
        }
    dispatch['default'] = dispatch[DEFAULT_STEMMER]

    def __init__(self, options):
        self.options = options

    def stem(self):
        stemmer = self.options.get('stemmer', DEFAULT_STEMMER)
        stemmer_obj = self.dispatch.get(stemmer, self.dispatch[DEFAULT_STEMMER])

        if stemmer_obj == SnowballStemmer:
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


class NLTKTokenize(object):
    dispatch = {
            'word': word_tokenize,
            'string': StringTokenizer,
            'tweet': TweetTokenizer,
            }
    dispatch['default'] = dispatch[DEFAULT_TOKENIZER]

    def __init__(self, options):
        self.options = options

    def tokenize(self):
        tokenizer = self.options.get('tokenizer', DEFAULT_TOKENIZER)
        tokenizer_obj = self.dispatch.get(tokenizer, self.dispatch[DEFAULT_TOKENIZER])

        print tokenizer, tokenizer_obj
        if tokenizer_obj == word_tokenize:
            result = tokenizer_obj(self.options['string'])

        else:
            result = tokenizer_obj().tokenize(self.options['string'])

        return self._dump(result)

    def _dump(self, result):
        response = {
                'status': True,
                'result': result
                }
        return response
