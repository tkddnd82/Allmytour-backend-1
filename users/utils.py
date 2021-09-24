import jwt
import bcrypt
import json
import string
import random
import sys
import os
import hashlib
import hmac
import base64
import requests
import time

from django.http.response   import JsonResponse
from my_settings            import SECRET_KEY,ACCESS_KEY, FROM_PHONE_NUMBER, URI,URL
from users.models           import User



def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
            user         = User.objects.get(id=payload['id'])
            request.user = user
            
        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE' : 'INVALID_TOKEN'}, status=400)
            
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=400)
        return func(self, request, *args, **kwargs)
    return wrapper