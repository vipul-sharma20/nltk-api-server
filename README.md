nltk-api-server
===============

API server for NLTK. Aimed to provide convenient interface to use NLTK over
any programming language

Features
========
* Stemming
* Lemmatization
* Part of Speech Tagging (Unigram/Bigram/Regex)
* Named Entity Recognition
* Sentiment Analysis

---------------
**1. Stemming**
---------------

NLTK Stemmers used: Porter, Snowball and Lancaster

* **Accepts:**

  * `/api/stem?words=<words>/`

  * `/api/stem?words=<words>&stemmer=<porter/snowball/lancaster/default>/`

  * `/api/stem?words=<words>&stemmer=snowball&language=<language>&ignore_stopwords=<true/false>/`

* **Query Parameters:**

  * Mandatory:
      * `words`:

          ***value:*** string comma separated
  * Optional:
      * `stemmer`:

          ***value:*** porter/snowball/lancaster/default

          ***default:*** snowball

      * `ignore_stopwords`: Only for Snowball Stemmer

           ***value:*** true/false

           ***default:*** false

      * `language`: Only for Snowball Stemmer

           ***value:*** see SnowballStemmer.languages

           ***default:*** english

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

* The above examples do not cover all cases. See the section above examples
  for more features

--------------------
**2. Lemmatization**
--------------------

NLTK Lemmatizer used: WordNetLemmatizer

* **Accepts:**

  * `/api/lemma?words=<words>/`

* **Query Parameters:**
   * Mandatory:
       * `words`:

           ***value:*** string comma separated

------------
2.1 Examples
------------
* `localhost/api/lemma/?words=dogs,cats,vertices`

        {
            "status":true,
            "result": [
                "dog",
                "cat",
                "vertex"
            ]
        }

-----------------------------
**3. Part of Speech Tagging**
-----------------------------

NLTK POS tagger used: pos_tag, UnigramTagger, BigramTagger & RegexpTagger

* **Accepts:**

  * `/api/tag?sentence=<sentence>/`

  * `/api/tag?sentence=<sentence>&tagger=<pos/unigram/bigram/default>/`

  * `/api/tag?sentence=<sentence>&tagger=<pos/unigram/bigram/default>&train=<categories>/`

  including any query parameter accepted by /api/tag/

* **Query Parameters:**

  * Mandatory:
      * `sentence`:

          ***value:*** string

  * Optional:

      * `tagger`:

          ***value:*** pos/unigram/bigram/regex

          ***default:*** pos_tag

      * `train` (iff unigram/bigram):

          ***value:*** 'news', 'editorial', 'reviews', 'religion',
                 'learned', 'science_fiction', 'romance', 'humor'

          ***default:*** 'news'

      * **any query parameter acceptable by /api/tag/**

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

* The above examples do not cover all cases. See the section above examples
  for more features
* **Remember, we can also use trained data along with the unigram/bigram tagger:
    'news', 'editorial', 'reviews', 'religion', 'learned', 'science_fiction', 'romance', 'humor'**

-------------------------------
**4. Named Entity Recognition**
-------------------------------

NLTK NER used: ne_chunk

* Accepts:

  * `/api/ner?sentence=<sentence>/`

  including any query parameter accepted by /api/tag/

* Query Parameters:

  * Mandatory:
      * `sentence`:

          ***value:*** string

      * Optional:

          * **any query parameter acceptable by /api/tag/**

------------
4.1 Examples
------------

* `localhost/api/ner?sentence=At the Olympics in August, Phelps picked up five gold medal`

        {
            "status": true,
            "result": [
                "Phelps"
            ]
        }

-------------------------
**5. Sentiment Analysis**
-------------------------

NLTK Sentiment Analyzer used: vader

* **Accepts:**

  * `/api/sentiment?sentence=<sentence>/`

* **Query Parameters:**

  * Mandatory:
      * `sentence`:

           ***value:*** string

  * Optional:

      * **any query parameter acceptable by /api/tag/**

------------
5.1 Examples
------------

* `localhost/api/sentiment?sentence=At the Olympics in August, Phelps picked up five gold medal`

        {
            "status": true,
            "result": {
                "neg": 0,
                "neu": 0.256,
                "pos": 0.744,
                "compound": 0.4404
            }
        }

-------------------
**6. Run on local**
-------------------

* `git clone git@github.com:vipul-sharma20/nltk-api-server.git`
* `cd nltk-api-server`
* `sudo pip install virtualenv`
     * Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already.
     * If you don't have pip installed, visit here to see steps to install virtualenv: [https://virtualenv.readthedocs.org/en/latest/installation.html](https://virtualenv.readthedocs.org/en/latest/installation.html)
* `virtualenv nltk-api`
* `source nltk-api/bin/activate`
* `pip install -r requirements.txt` (wait till the requirements are installed)
* `python manage.py runserver` This will run the application on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**IMPORTANT:** You will require some corpora and trained models
for the code to run. You can refer to: [http://www.nltk.org/data.html](http://www.nltk.org/data.html)

* Interactive Method:

        In [1]: import nltk

        In [2]: nltk.download()
