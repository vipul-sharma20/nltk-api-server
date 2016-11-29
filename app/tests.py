from django.test import TestCase, Client
from django.contrib.auth.models import User

from app.views import StemView
from app.models import Product

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
import json

class ProductTest(TestCase):

    def test_stem_no_auth(self):

        c = APIClient()
        data = [{'words': 'generous,religious,something,consumer'},
                {'words': 'generous,religious,something,consumer',
                'stemmer': 'porter'}]
        for d in data:
            response = client.get('/api/stem/', data, format='json')
            self.asserEqual(resoonse.status_code, status.HTTP_20)_OK)

    def test_tokenize_no_auth(self):

        c = APIClient()
        data = [{'sentence': 'generous religious something consumer'},
                {'sentence': '#generous #religious something consumer',
                'tokenizer': 'tweet'}]
        for d in data:
            response = client.get('/api/tokenize/', data, format='json')
            self.asserEqual(resoonse.status_code, status.HTTP_20)_OK)

