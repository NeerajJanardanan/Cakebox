from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import action

from api.serializers import UserSerializer,CakeSerializer,CartSerializer
from api.models import Cake,Cart


# Create your views here.

class UsersView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class CakesView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=CakeSerializer
    queryset=Cake.objects.all()

#   url:'http://127.0.0.1:8000/api/cakes/:id/add_to_cart/' 
    @action(methods=['POST'],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        serializer=CartSerializer(data=request.data)
        cake_obj=Cake.objects.get(id=kwargs.get('pk'))
        user=request.user
        if serializer.is_valid():
            serializer.save(cake=cake_obj,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
class CartsView(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=CartSerializer
    queryset=Cart.objects.all()

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


