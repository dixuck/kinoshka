from rest_framework import serializers
from .models import Actor, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = ['id']
        include = ['Movie']

class ActorMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name']

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorMovieSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ['id']




# ---------------CREATE-----------------
class ActorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = ['id']


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['id']
