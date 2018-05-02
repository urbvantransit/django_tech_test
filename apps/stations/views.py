# coding: utf8

from django.urls import reverse_lazy
from .models import LocationModel, StationModel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# CRUD LOCATIONS
class LocationListView(ListView):
    model = LocationModel

    def get_queryset(self):
        queryset = super(LocationListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LocationListView, self).get_context_data(**kwargs)
        return context


class LocationCreateView(CreateView):
    model = LocationModel
    fields = ('name', 'latitude', 'longitude')
    success_url = reverse_lazy('locations:list')

    def get_context_data(self, **kwargs):
        context = super(LocationCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        form.save()
        return super(LocationCreateView, self).form_valid(form)


class LocationUpdateView(UpdateView):
    model = LocationModel
    fields = ('name', 'latitude', 'longitude')
    success_url = reverse_lazy('locations:list')

    def get_context_data(self, **kwargs):
        context = super(LocationUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super(LocationUpdateView, self).form_valid(form)


class LocationDeleteView(DeleteView):
    model = LocationModel
    success_url = reverse_lazy('locations:list')

    def get_context_data(self, **kwargs):
        context = super(LocationDeleteView, self).get_context_data(**kwargs)
        data = {
            'name': self.object,
        }
        context.update(data)
        return context

    def delete(self, request, *args, **kwargs):
        return super(LocationDeleteView, self).delete(request, *args, **kwargs)


# CRUD STATIONS
class StationListView(ListView):
    model = StationModel

    def get_queryset(self):
        queryset = super(StationListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(StationListView, self).get_context_data(**kwargs)
        return context


class StationCreateView(CreateView):
    model = StationModel
    fields = ('id', 'location', 'order', 'is_active')
    success_url = reverse_lazy('stations:list')

    def get_context_data(self, **kwargs):
        context = super(StationCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        form.save()
        return super(StationCreateView, self).form_valid(form)


class StationUpdateView(UpdateView):
    model = StationModel
    fields = ('id', 'location', 'order', 'is_active')
    success_url = reverse_lazy('stations:list')

    def get_context_data(self, **kwargs):
        context = super(StationUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super(StationUpdateView, self).form_valid(form)


class StationDeleteView(DeleteView):
    model = StationModel
    success_url = reverse_lazy('stations:list')

    def get_context_data(self, **kwargs):
        context = super(StationDeleteView, self).get_context_data(**kwargs)
        data = {
            'id': self.object,
        }
        context.update(data)
        return context

    def delete(self, request, *args, **kwargs):
        return super(StationDeleteView, self).delete(request, *args, **kwargs)