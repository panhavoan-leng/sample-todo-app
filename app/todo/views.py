from django.shortcuts import render
from rest_framework import serializers

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TodoSerializer
from .models import Todo


class TodoView(
    viewsets.ViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):

    queryset = Todo.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["is_completed"]
    search_fields = ["title"]
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

    def delete_todo(self, request, id=None):
        self.destroy(request)
        return Response({"message": "OK"})

    def mark_as_complete(self, request, id=None):
        instance = self.get_object()
        instance.is_completed = True
        instance.save()
        return Response({"message": "OK"})
