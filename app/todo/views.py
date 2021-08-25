from django.shortcuts import render
from rest_framework import serializers

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoView(
    viewsets.ModelViewSet,
):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"

    def list_todo(self, request):
        return self.list(request)

    def detail_todo(self, request, id=None):
        return self.retrieve(request)

    def post(self, request):
        return self.create(request)

    def update_todo(self, request, id=None):
        return self.update(request)
