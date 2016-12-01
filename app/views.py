from rest_framework.views import APIView
from rest_framework.response import Response

from util import NLTKStem, NLTKTokenize, NLTKTag, NLTKner


class HomeView(APIView):
    """
    Landing Page View
    """

    """
    /api/tokenize?sentence=<sentence>/
    /api/tokenize?sentence=<sentence>&tokenizer=<word/tweet/default>/
    /api/ner?sentence=<sentence>/
    """
    def get(self, request):
        res = {
            'endpoints': [
                '/api/stem?words=<word1,word2,word3>/',
                '/api/stem?words=<word1,word2>&stemmer=<porter/snowball/lancaster/default>/',
                '/api/stem?words=<word1,word2>&stemmer=snowball&language<language>&ignore_stopwords=<true/false>/',
                '/api/tag?sentence=<sentence>/',
                '/api/tag?sentence=<sentence>&tagger=<pos/unigram/bigram>/',
                '/api/tag?sentence=<sentence>&tagger=<pos/unigram/bigram>&train=<categories>',
                '/api/'
            ],
            'message': 'see app/util.py for details',
            'repository': 'https://github.com/vipul-sharma20/nltk-api-server',
        }
        return Response(res)


class StemView(APIView):
    """
    View for Stemming words
    """

    def get(self, request):
        data = request.GET

        if not data.get('words'):
            return Response({
                'message': 'words parameter missing',
                'status': False,
            })

        stem_obj = NLTKStem(data)

        res = stem_obj.stem()
        return Response(res)


class TokenizeView(APIView):
    """
    View for Tokenizing strings
    """

    def get(self, request):
        data = request.GET

        if not data.get('sentence'):
            return Response({
                'message': 'sentence parameter missing',
                'status': False
            })

        tokenize_obj = NLTKTokenize(data)
        res = tokenize_obj.tokenize()

        return Response(res)


class POSTagView(APIView):
    """
    View for Part Of Speech tagging
    """

    def get(self, request):
        data = request.GET

        if not data.get('sentence'):
            return Response({
                'message': 'sentence parameter missing',
                'status': False
            })

        pos_obj = NLTKTag(data)
        res = pos_obj.pos_tag()

        return Response(res)


class NERView(APIView):
    """
    View for Named Entity Recognition
    """

    def get(self, request):
        data = request.GET

        if not data.get('sentence'):
            return Response({
                'message': 'sentence parameter missing',
                'status': False
            })

        ner_obj = NLTKner(data)
        res = ner_obj.ner()

        return Response(res)

