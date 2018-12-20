from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LineModel


class LineModelList(ListView):
    model = LineModel
    fields = ['name', 'color']


class LineModelCreate(CreateView):
    model = LineModel
    fields = ['name', 'color']
    success_url = reverse_lazy('line_model_list_view')
    template_name_suffix = '_create_form'


class LineModelDetail(UpdateView):
    model = LineModel
    template_name_suffix = '_update_form'
    fields = ['name', 'color']
    success_url = reverse_lazy('line_model_list_view')


class LineModelDelete(DeleteView):
    model = LineModel
    success_url = reverse_lazy('line_model_list_view')
    template_name_suffix = '_delete_form'
