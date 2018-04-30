# coding: utf8
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import LocationModel


class LocationListView(ListView):
    model = LocationModel

    def get_queryset(self):
        queryset = super(LocationListView, self).get_queryset()
        queryset = queryset.filter(active=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LocationListView, self).get_context_data(**kwargs)
        data = {
            'title': 'Location list',
            'description': 'This in the list of locations',
        }
        context.update(data)
        return context


class LocationCreateView(CreateView):
    model = LocationModel
    fields = ('name', 'key', 'latitude', 'longitude')
    success_url = reverse_lazy('locations:list')

    def get_context_data(self, **kwargs):
        context = super(LocationCreateView, self).get_context_data(**kwargs)
        data = {
            'title': 'Create location',
            'description': 'Complete the next fields please',
            'button_legend': 'Create location',
        }
        context.update(data)
        return context

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        new_location = form.save()
        messages.success(self.request, '%s successfull created' % new_location )
        return super(LocationCreateView, self).form_valid(form)


class LocationUpdateView(UpdateView):
    model = LocationModel
    fields = ('name', 'key', 'latitude', 'longitude')
    success_url = reverse_lazy('locations:list')

    def get_context_data(self, **kwargs):
        context = super(LocationUpdateView, self).get_context_data(**kwargs)
        title = "Update location"
        button_legend = 'update location'
        description = 'Update the next information'
        data = {
            'title': title,
            'description': description,
            'button_legend': button_legend,
        }
        context.update(data)
        return context

    def form_valid(self, form):
        location_updated = form.save()
        messages.success(self.request, '%s successfull updated' % location_updated)
        return super(LocationUpdateView, self).form_valid(form)


class LocationDeleteView(DeleteView):
    model = LocationModel
    success_url = reverse_lazy('locations:list')
    success_message = 'Location delete successfull'

    def get_context_data(self, **kwargs):
        context = super(LocationDeleteView, self).get_context_data(**kwargs)
        title = "Delete location"
        button_legend = 'delete location'
        description = 'Do you really whant delete %s' % (self.object)
        data = {
            'title': title,
            'description': description,
            'button_legend': button_legend,
        }
        context.update(data)
        return context

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(LocationDeleteView, self).delete(request, *args, **kwargs)