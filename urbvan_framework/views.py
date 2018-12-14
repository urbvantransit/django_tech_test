# coding: utf8
from django.http import Http404
from rest_framework import generics

from .mixins import (
    CreateModelMixin,
    ListModelMixin)
from .schemas import PaginationResponse


class CreateAPIView(CreateModelMixin, generics.GenericAPIView):
    """
    Concrete view for creating a model instance.
    """

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(ListModelMixin, generics.GenericAPIView):
    """
    Concrete view for listing a queryset.
    """
    pagination_class = PaginationResponse

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #TODO: Add search capabilities

class ListCreateView(CreateAPIView, ListAPIView):
    pass


class DetailViewMixin(object):
    """ Mixin that overrides the standard get_object method from REST Framework"""

    def get_object(self, pk=None):
        """
            :return: A model instance given a pk in self.kwargs
        """
        try:
            if pk is not None:
                return self.model.objects.get(pk=pk)
            else:
                return self.model.objects.get(pk=self.kwargs.get('pk'))
        except self.model.DoesNotExist:
            raise Http404


class DetailView(DetailViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Concrete view for Retrieve, update or delete an instance.
    """
