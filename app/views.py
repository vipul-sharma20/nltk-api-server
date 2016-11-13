from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from util import NLTKStem


class StemView(APIView):

    def get(self, request):
        data = request.GET
        st = NLTKStem(data)
        result = st.stem()
        return Response({'test': result})
