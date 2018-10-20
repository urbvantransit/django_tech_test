from django.shortcuts import render,get_object_or_404
# Create your views here.
# We're gonna create a CRUD app with Class Based Views
# Import the inherited classes
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Im gonna import the Models and Forms to build the Views
from .models import Users
from .forms import UsersModelForm

# I'm gonna build a new classes to manage my models created an apply CRUD
class UsersListView(ListView):
    queryset = Users.objects.all()
    template_name = 'users/users_list.html'

class UsersDetailView(DetailView):
    queryset = Users.objects.all()
    template_name = 'users/users_detail.html'

class UsersCreateView(CreateView):
    pass

class UsersUpdateView(UpdateView):
    pass

class UsersDeleteView(DeleteView):
    pass
