from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import jwt
from django.conf import settings
from .serializer import UserSerializer
# Create your views here.



class LogInView(APIView):
    def post(self,request):
        try:
            userObject=User.objects.get(username=request.data['username'])
            
            if userObject.check_password(request.data['password']):
                # build a payload
                payload={
                            "username":userObject.username,
                            "id":userObject.pk
                        }
                # generate the jwt Token
<<<<<<< HEAD
                jwt_token=jwt.encode(
                                        payload=payload,
                                        key=settings.JWT_SECRET,
                                        headers={"alg": "HS256","typ": "JWT"}
                                    )
=======
                jwt_token=jwt.encode(payload=payload,key=settings.JWT_SECRET)
>>>>>>> 80bc9ff6232c54c345c73b938e0ac50b391fc199
        
                return Response({'user':userObject.username,'jwt_token':jwt_token},status=status.HTTP_200_OK)
            else:
                return Response({"error":"Invalid username/password..."},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_401_UNAUTHORIZED)
                

class RegistrationView(APIView):
    def post(self,request):
        try:
            serialisedUserData=UserSerializer(data=request.data)
            if serialisedUserData.is_valid():
                serialisedUserData.save()
                return Response({
                    "username":serialisedUserData.data['username'],
                    "password":request.data.get('password'),
                    "message":"User registration successfull !"
                    },status=status.HTTP_201_CREATED)
            else:
                return Response("User Creation Failed...",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    # pass
