# coding: utf8

from django.urls import reverse_lazy
from .models import LineModel, RouteModel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# CRUD LINES
class LineListView(ListView):
    model = LineModel

    def get_queryset(self):
        queryset = super(LineListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LineListView, self).get_context_data(**kwargs)
        return context


class LineCreateView(CreateView):
    model = LineModel
    fields = ('name', 'color')
    success_url = reverse_lazy('lines:list')

    def get_context_data(self, **kwargs):
        context = super(LineCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        form.save()
        return super(LineCreateView, self).form_valid(form)


class LineUpdateView(UpdateView):
    model = LineModel
    fields = ('name', 'color')
    success_url = reverse_lazy('lines:list')

    def get_context_data(self, **kwargs):
        context = super(LineUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super(LineUpdateView, self).form_valid(form)


class LineDeleteView(DeleteView):
    model = LineModel
    success_url = reverse_lazy('lines:list')

    def get_context_data(self, **kwargs):
        context = super(LineDeleteView, self).get_context_data(**kwargs)
        data = {
            'name': self.object,
        }
        context.update(data)
        return context

    def delete(self, request, *args, **kwargs):
        return super(LineDeleteView, self).delete(request, *args, **kwargs)


# CRUD ROUTES
class RouteListView(ListView):
    model = RouteModel

    def get_queryset(self):
        queryset = super(RouteListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(RouteListView, self).get_context_data(**kwargs)
        return context


class RouteCreateView(CreateView):
    model = RouteModel
    fields = ('line', 'stations', 'direction', 'is_active')
    success_url = reverse_lazy('routes:list')

    def get_context_data(self, **kwargs):
        context = super(RouteCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        form.save()
        return super(RouteCreateView, self).form_valid(form)


class RouteUpdateView(UpdateView):
    model = RouteModel
    fields = ('line', 'stations', 'direction', 'is_active')
    success_url = reverse_lazy('routes:list')

    def get_context_data(self, **kwargs):
        context = super(RouteUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super(RouteUpdateView, self).form_valid(form)


class RouteDeleteView(DeleteView):
    model = RouteModel
    success_url = reverse_lazy('routes:list')

    def get_context_data(self, **kwargs):
        context = super(RouteDeleteView, self).get_context_data(**kwargs)
        data = {
            'id': self.object,
        }
        context.update(data)
        return context

    def delete(self, request, *args, **kwargs):
        return super(RouteDeleteView, self).delete(request, *args, **kwargs)