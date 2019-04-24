# coding: utf-8
from rest_framework import authentication


class CustomTokenAuthentication(authentication.TokenAuthentication):
    keyword = 'Urbvan'
