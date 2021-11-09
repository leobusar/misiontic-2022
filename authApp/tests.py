from django.test import TestCase
import json
import jwt 

from rest_framework import status
from rest_framework.test import APIClient

class TestAPI(TestCase):
    def test_signUp(self):
        client = APIClient()
        response = client.post('/user/', 
        {
            "username": "user_prueba_1",
            "password": "password_prueba_1",
            "name": "user prueba",
            "email": "user_prueba_1@misionTIC.com",
            "account": {
                "lastChangeDate": "2021-09-23T10:25:43.511Z",
                "balance": 20000,
                "isActive": "true"
            }
        },
        format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('refresh' in response.data.keys(), True)
        self.assertEqual('access' in response.data.keys(), True)
    
    def test_login(self):
        client = APIClient()
        response = client.post('/login/', 
        {
            "username": "Leonardo",
            "password": "hello12",
        },
        format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('refresh' in response.data.keys(), True)
        self.assertEqual('access' in response.data.keys(), True)        
        
    def test_user(self):
        client = APIClient()
        response = client.post('/login/', 
        {
            "username": "Leonardo",
            "password": "hello12",
        },
        format='json')
        token = response.data['access']

        secret='django-insecure-sx9y!yj7(ghnhsars*su0f82^jma0h*&v%62b6@n!&l3i%^20g'
        user_id = jwt.decode(token, secret, algorithms=['HS256'])['user_id']
        
        url = '/user/'+str(user_id)+'/'
        auth_headers = {'HTTP_AUTHORIZATION': 'Bearer '+token}

        response = client.get(url, **auth_headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'Leonardo')