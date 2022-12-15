from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import MovesSerializer,DramaSerializer,ActionSerializer,AnimationSerializer
# Create your views here.
from .models import Move,Drama,Action,Animation
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class MoveListView(ListCreateAPIView):
   queryset=Move.objects.all()
   serializer_class=MovesSerializer
   permission_classes=[IsAuthenticatedOrReadOnly]

class DramaListView(ListCreateAPIView):
   queryset=Drama.objects.all()
   serializer_class=DramaSerializer
   permission_classes=[IsAuthenticated]

class ActionListView(ListCreateAPIView):
   queryset=Action.objects.all()
   serializer_class=ActionSerializer
   permission_classes=[IsAuthenticated]

class AnimationListView(ListCreateAPIView):
   queryset=Animation.objects.all()
   serializer_class=AnimationSerializer
   permission_classes=[IsAuthenticated]


class DramaDetailView(RetrieveUpdateDestroyAPIView):
   queryset=Drama.objects.all()
   serializer_class= DramaSerializer
   permission_classes=[IsOwnerOrReadOnly,IsAuthenticated]  # this page display for the registered user and the just the owner can edit it


class ActionDetailView(RetrieveUpdateDestroyAPIView):
   queryset=Action.objects.all()
   serializer_class= ActionSerializer
   permission_classes=[IsOwnerOrReadOnly,IsAuthenticated]  # this page display for the registered user and the just the owner can edit it

class AnimationDetailView(RetrieveUpdateDestroyAPIView):
   queryset=Animation.objects.all()
   serializer_class= AnimationSerializer
   permission_classes=[IsOwnerOrReadOnly,IsAuthenticated]  # this page display for the registered user and the just the owner can edit it