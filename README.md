========
nltk-api
========

API server for NLTK. Aimed to provide convenient interface to use NLTK over
any programming language

Features
========
* Stemming
* Lemmatization
* Part of Speech Tagging (Unigram/Bigram/Regex)
* Named Entity Recognition
* Sentiment Analysis

------------
1. Stemming
------------

NLTK Stemmers used: Porter, Snowball and Lancaster

* Accepts:

  * `/api/stem?words=<words>/`

  * `/api/stem?words=<words>&stemmer=<porter/snowball/lancaster/default>/`

  * `/api/stem?words=<words>&stemmer=snowball&language=<language>&ignore_stopwords=<true/false>/`

* Query Parameters:

  * Mandatory:
      1. `words`:
          type: string comma separated
  * Optional:
      1. `stemmer`:
          value: porter/snowball/lancaster/default
          default: snowball
      2. `ignore_stopwords`: Only for Snowball Stemmer
           value: true/false
           default: false
      3. `language`: Only for Snowball Stemmer
           value: see SnowballStemmer.languages
           default: english

------------
1.1 Examples
------------

* `localhost:9000/api/stem?words=dangerous,monitoring,testing`

    {
	"status": true,
	"result": [
	    "danger",
	    "monitor",
	    "test"
	]
   }

* `localhost:9000/api/stem/?words=dangerous,monitoring,testing&stemmer=snowball`


    {
        "status": true,
        "result": [
            "dog",
            "cat",
            "vertex"
        ]
    }

----------------
2. Lemmatization
----------------

NLTK Lemmatizer used: WordNetLemmatizer

* Accepts:
  * `/api/lemma?words=<words>/`

* Query Parameters:
   * Mandatory:
      1. `words`:

          type: string comma separated

------------
2.1 Examples
------------
* `localhost/api/lemma/?words=dogs,cats,vertices`

    {
        "status":true,
        "result":[
            "dog",
            "cat",
            "vertex"
        ]
    }

-------------------------
3. Part of Speech Tagging
-------------------------

NLTK POS tagger used: pos_tag, UnigramTagger, BigramTagger & RegexpTagger

* Accepts:

  * /api/tag?sentence=<sentence>/
  * /api/tag?sentence=<sentence>&tagger=<pos/unigram/bigram/default>/
  * /api/tag?sentence=<sentence>&tagger=<pos/unigram/bigram/default>&train=<categories>/

  including any query parameter accepted by /api/tag/

* Query Parameters:

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

     3. any query parameter acceptable by /api/tag/

------------
3.1 Examples
------------
* `localhost/api/sentence=this is a test`

	{
		"status": true,
		"result": [
			[
				"this",
				"DT"
			],
			[
				"is",
				"VBZ"
			],
			[
				"a",
				"DT"
			],
			[
				"test",
				"NN"
			]
		]
	}

* `localhost/api/sentence=this is a test&tagger=unigram`

	{
		"status": true,
		"result": [
			[
				"this",
				"DT"
			],
			[
				"is",
				"BEZ"
			],
			[
				"a",
				"AT"
			],
			[
				"test",
				"NN"
			]
		]
	}

* **Remeber we can also use trained data alongwith the unigram/bigram tagger:
    'news', 'editorial', 'reviews', 'religion', 'learned', 'science_fiction', 'romance', 'humor'**
