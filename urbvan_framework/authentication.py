from rest_framework import authentication


class CustomTokenAuthentication(authentication.TokenAuthentication):
    keyword = 'Urbvan'
