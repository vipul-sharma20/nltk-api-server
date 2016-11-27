from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from util import NLTKStem, NLTKTokenize, NLTKTag


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

