from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer

from nltk import word_tokenize, pos_tag, UnigramTagger, BigramTagger, RegexpTagger
from nltk.tokenize import TweetTokenizer
from nltk.corpus import brown

from app.constants import DEFAULT_STEMMER, DEFAULT_TOKENIZER, DEFAULT_TAGGER, \
    DEFAULT_TRAIN, TRAINERS


class NLTKStem(object):
    """
    NLTK Stemmers used: Porter, Snowball and Lancaster

    Accepts:

    /api/stem?words=<words>/
    /api/stem?words=<words>&stemmer=<porter/snowball/lancaster/default>/
    /api/stem?words=<words>&stemmer=snowball&language=<language>&ignore_stopwords=<true/false>/

    Query Parameters:

        * Mandatory:
            1. words:
                type: string comma separated
        * Optional:
            1. stemmer:
                value: porter/snowball/lancaster/default
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
        words = self._clean(self.options['words'])
        stemmer = self.options.get('stemmer', DEFAULT_STEMMER)
        stemmer_obj = self.dispatch.get(stemmer, self.dispatch[DEFAULT_STEMMER])
        result = []

        if stemmer_obj == SnowballStemmer:
            ignore_stopwords = False

            if self.options.get('ignore_stopwords'):
                if self.options['ignore_stopwords'] == 'true':
                    ignore_stopwords = True
            language = self.options.get('language', 'english')

            for word in words:
                result.append(
                    stemmer_obj(language, ignore_stopwords).stem(word))

        else:
            for word in words:
                result.append(stemmer_obj().stem(word))

        return self._dump(result)

    def _clean(self, words):
        return words.split(',')

    def _dump(self, result):
        response = {
            'status': True,
            'result': result
        }
        return response


class NLTKTokenize(object):
    """
    NLTK Tokenizers used: word_tokenize, StringTokenizer, TweetTokenizer

    Accepts:

    /api/tokenize?sentence=<sentence>/
    /api/tokenize?sentence=<sentence>&tokenizer=<word/tweet/default>/

    Query Parameters:

        * Mandatory:
            1. sentence:
                type: string
        * Optional:
            1. tokenizer:
                value: word/tweet/default
                default: word_tokenize
    """

    dispatch = {
        'word': word_tokenize,
        'tweet': TweetTokenizer,
    }
    dispatch['default'] = dispatch[DEFAULT_TOKENIZER]

    def __init__(self, options):
        self.options = options

    def tokenize(self):
        tokenizer = self.options.get('tokenizer', DEFAULT_TOKENIZER)
        tokenizer_obj = self.dispatch.get(tokenizer,
                                          self.dispatch[DEFAULT_TOKENIZER])

        if tokenizer_obj == word_tokenize:
            result = tokenizer_obj(self.options['sentence'])

        else:
            result = tokenizer_obj().tokenize(self.options['sentence'])

        return self._dump(result)

    def _dump(self, result):
        response = {
            'status': True,
            'result': result
        }
        return response


class NLTKTag(object):
    """
    NLTK POS tagger used: pos_tag

    Accepts:

    /api/tag?sentence=<sentence>/
    /api/tag?sentence=<sentence>&tagger=<pos/unigram/bigram/default>/
    /api/tag?sentence=<sentence>&tagger=<pos/unigram/bigram/default>&train=<categories>/


    Query Parameters:

        * Mandatory:
            1. sentence:
                type: string

        * Optional:
            1. tagger:
                value: pos/unigram/bigram/regex
                default: pos_tag
            2. train (iff unigram/bigram):
                value: 'news', 'editorial', 'reviews', 'religion',
                       'learned', 'science_fiction', 'romance', 'humor'
                default: 'news'
    """

    def __init__(self, options):
        self.options = options

    def pos_tag(self):
        tokenize_obj = NLTKTokenize(self.options)
        res = tokenize_obj.tokenize()
        tokens = res['result']
        tags = []

        if self.options.get('tagger') in ['unigram', 'bigram', 'regex']:
            if self.options.get('train') in TRAINERS:
                train = brown.tagged_sents(categories=self.options['train'])
            else:
                train = brown.tagged_sents(categories=DEFAULT_TRAIN)

            # Create your custom regex tagging pattern here
            regex_tag = RegexpTagger([
                (r'^[-\:]?[0-9]+(.[0-9]+)?$', 'CD'),
                (r'.*able$', 'JJ'),
                (r'^[A-Z].*$', 'NNP'),
                (r'.*ly$', 'RB'),
                (r'.*s$', 'NNS'),
                (r'.*ing$', 'VBG'),
                (r'.*ed$', 'VBD'),
                (r'.*', 'NN')
            ])
            unigram_tag = UnigramTagger(train, backoff=regex_tag)
            if self.options['tagger'] == 'bigram':
                bigram_tag = BigramTagger(train, backoff=unigram_tag)
                tags = bigram_tag.tag(tokens)
            elif self.options['tagger'] == 'unigram':
                tags = unigram_tag.tag(tokens)
            else:
                tags = regex_tag.tag(tokens)

        elif self.options.get('tagger', DEFAULT_TAGGER) == 'pos':
            tags = pos_tag(tokens)

        return self._dump(tags)

    def _dump(self, result):
        response = {
            'status': True,
            'result': result
        }
        return response
