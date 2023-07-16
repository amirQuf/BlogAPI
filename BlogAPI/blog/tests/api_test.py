from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post


class YourAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Setup any required data or objects for the tests
        pass

    def test_create_resource(self):
       response = self.client.post('/post/', {'title': 'test'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(YourModel.objects.count(), 1)
        self.assertEqual(YourModel.objects.get().name, 'Test Resource')
