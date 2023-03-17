from django.shortcuts import render
<<<<<<< HEAD
from rest_framework.response import Response
from .models import TodoTask
from rest_framework.views import APIView
from rest_framework import status
from .serializer import TaskSerializer
from rest_framework.authentication import get_authorization_header
import jwt
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .jwtAuth import JWTAuthentication
from django.conf import settings

# Create your views here.



class taskViewSet(APIView):  
    def get(self,request):
        username,authToken=JWTAuthentication(request)
        if username and authToken and username!=None:
            user=User.objects.get(username=username)
            allData=TodoTask.objects.filter(createdBy=user)
            SerialisedData=TaskSerializer(allData,many=True)
            return Response(SerialisedData.data,status=status.HTTP_200_OK)
        else: return Response({"error":"authentication failed"},status=status.HTTP_401_UNAUTHORIZED)
    

    def post(self,request):
        username,authToken=JWTAuthentication(request)
        if username and authToken and username!=None:
            user=User.objects.get(username=username)
            request.data['createdBy']=user.pk #externally adding the user.pk to the foreignkey [here reques.data is a dict]
            DeserializedData=TaskSerializer(data=request.data)
            # DeserializedData['createdBy']=user.pk
            try:
                if DeserializedData.is_valid():
                    DeserializedData.save()
                    return Response(DeserializedData.data,status=status.HTTP_201_CREATED)
                else:
                    return Response({'error':"Invalid data passed"},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        else: return Response({"error":"authentication failed"},status=status.HTTP_401_UNAUTHORIZED)
    
    
class taskSearchView(APIView):

    def get(self,request,onDate:str):
        username,authToken=JWTAuthentication(request)
        if username and authToken and username!=None:
            user=User.objects.get(username=username)
            allData=TodoTask.objects.filter(createdBy=user,createdOn=onDate)
            SerialisedData=TaskSerializer(allData,many=True)
            return Response(SerialisedData.data,status=status.HTTP_200_OK)
        else: return Response({"error":"authentication failed"},status=status.HTTP_401_UNAUTHORIZED)
    
    # 15/03/2023
    # Update Api
class taskUpdateView(APIView):

    def patch(self, request,id:int):
        username,authToken=JWTAuthentication(request)
        if username and authToken and username!=None:
            user=User.objects.get(username=username)
            try:
                taskData=TodoTask.objects.get(id=id,createdBy=user.pk)  
                taskSerializedData=TaskSerializer(taskData,data=request.data,partial=True)
                if taskSerializedData.is_valid():
                    taskSerializedData.save()
                    return Response(taskSerializedData.data,status=status.HTTP_202_ACCEPTED)
                else:
                    return Response({"erroe":"Serializer Validation failed !"},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(str(e))
        else: return Response({"error":"authentication failed"},status=status.HTTP_401_UNAUTHORIZED)
    
        
        


    # Delete Api
    def delete(self,request,id:int):
        username,authToken=JWTAuthentication(request)
        if username and authToken and username!=None:
            try:
                user=User.objects.get(username=username)
                taskData=TodoTask.objects.get(id=id,createdBy=user.pk)
                taskData.delete()
                return Response({'message':"data has been successfully removed !"},status= status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        else: return Response({"error":"authentication failed"},status=status.HTTP_401_UNAUTHORIZED)
        




=======

# Create your views here.
>>>>>>> 80bc9ff6232c54c345c73b938e0ac50b391fc199
