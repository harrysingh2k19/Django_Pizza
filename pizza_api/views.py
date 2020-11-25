from django.shortcuts import render
from rest_framework import generics
from .models import piza_type
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
	queryset = piza_type.objects.all()
	serializer_class = PostSerializer

class Input(generics.ListCreateAPIView):
	queryset = piza_type.objects.all()
	serializer_class = PostSerializer

# class Update(generics.RetrieveUpdateAPIView):
# 	queryset = piza_type.objects.all()
# 	serializer_class = PostSerializer

class Remove(generics.RetrieveUpdateDestroyAPIView):
	queryset = piza_type.objects.all()
	serializer_class = PostSerializer

