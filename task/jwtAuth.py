# from django.contrib.auth.models import User
import jwt
from rest_framework.authentication import get_authorization_header
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BaseAuthentication

def JWTAuthentication(request):
    try:
        username=request.user
        if not username:
            return (None,None)
        auth=get_authorization_header(request=request).split()
        if len(auth)!=2:
            raise Exception("Invalide Token field")
        payload=jwt.decode(auth[-1],settings.JWT_SECRET,algorithms=["HS256"])
        return (payload['username'],auth[-1])
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_401_UNAUTHORIZED)
    




