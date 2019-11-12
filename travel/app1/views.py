from django.shortcuts import render
from .models import destination
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import destinationSerializer

# Create your views here.
def index(request):

    dests = destination.objects.all()

    return render(request,'index.html', {'dests' : dests})


class destinationlist(APIView):
    def get(self,request):
        destination1 = destination.objects.all()
        serializer = destinationSerializer(destination1, many = True)
        return Response(serializer.data)