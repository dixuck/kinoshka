from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Actor, Movie
from .serializers import ActorSerializer, MovieSerializer, ActorCreateSerializer, MovieCreateSerializer


class ActorView(APIView):
    def get(self, request: Request):
        queryset = Actor.objects.all()
        serializer = ActorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class MovieView(APIView):
    def get(self, request: Request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActorCreateView(APIView):
    def post(self, request: Request):
        data = request.data
        serializer = ActorCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':('Created successfully', serializer.data)}, status=status.HTTP_201_CREATED)


class MovieCreateView(APIView):
    def post(self, request: Request):
        data = request.data
        serializer = MovieCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':('Created successfully', serializer.data)}, status=status.HTTP_201_CREATED)
