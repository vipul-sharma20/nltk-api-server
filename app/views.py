from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from util import NLTKStem, NLTKTokenize


class StemView(APIView):
    """
    View for Stemming words
    """

    def get(self, request):
        data = request.GET

        if not data.get('word'):
            return Response({
                'message': 'word parameter missing',
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

        if not data.get('string'):
            return Response({
                'message': 'string parameter missing',
                'status': False
                })

        tokenize_obj = NLTKTokenize(data)
        res = tokenize_obj.tokenize()

        return Response(res)

