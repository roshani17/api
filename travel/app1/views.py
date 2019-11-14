from django.shortcuts import render
from .models import destination, destinationName
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import destinationSerializer, UserSerializer,destinationNameSerializer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import permissions


from django.contrib.auth.models import User


# Create your views here.
def index(request):

    dests = destination.objects.all()

    return render(request,'index.html', {'dests' : dests})


class destinationlist(APIView):
    def get(self,request):
        destination1 = destination.objects.all()
        serializer = destinationSerializer(destination1, many = True)
        return Response(serializer.data)

    def post(self,request):
        print("in post method============================================")
        #data = JSONParser().parse(request)
        #print("data", data)
        serializer = destinationSerializer(data=request.data)
        print("serializer valid check" , serializer.is_valid())
        if serializer.is_valid():
            print("in serliazer func")
            serializer.save()
            print("in serliazer func", serializer)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class destinationNamelist(APIView):
    

    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        destination2 = destinationName.objects.all()
        serializer = destinationNameSerializer(destination2, many = True)
        return Response(serializer.data)

    def post(self,request):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
        #data = JSONParser().parse(request)
        #print("data", data)
        serializer = destinationNameSerializer(data=request.data)
        print("serializer valid check" , serializer.is_valid())
        if serializer.is_valid():
            print("in serliazer func")
            serializer.save()
            print("in serliazer func", serializer)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer






 