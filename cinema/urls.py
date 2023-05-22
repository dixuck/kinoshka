from django.urls import path

from .views import ActorView, MovieView, ActorCreateView, MovieCreateView

urlpatterns = [
                path('actors/', ActorView.as_view()),
                path('movies/', MovieView.as_view()),
                path('create-actor/', ActorCreateView.as_view()),
                path('create-movie/', MovieCreateView.as_view())
                ]
