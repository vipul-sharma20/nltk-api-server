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
    `{"status":true,"result":["danger","monitor","test"]}`
* `localhost:9000/api/stem/?words=dangerous,monitoring,testing&stemmer=snowball`
    `{"status":true,"result":["danger","monitor","test"]}`

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
    `{"status":true,"result":["dog","cat","vertex"]}`
