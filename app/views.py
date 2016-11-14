from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from util import NLTKStem


class StemView(APIView):
    """
    View for Stemming words
    """

    def get(self, request):
        data = request.GET

        if not data.get('word'):
            return Response({
                'message': 'word parameter missing',
                'status': False
                })

        stem_obj = NLTKStem(data)

        res = stem_obj.stem()
        return Response(res)

