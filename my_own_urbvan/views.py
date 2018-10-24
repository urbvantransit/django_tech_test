from django.shortcuts import render,get_object_or_404,reverse

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
class HomeView(ListView):
    queryset = Users.objects.all()
    template_name = 'users/home_view.html'

class UsersListView(ListView):
    queryset = Users.objects.all()
    template_name = 'users/users_list.html'

class UsersDetailView(DetailView):
    queryset = Users.objects.all()
    template_name = 'users/users_detail.html'

    # if get it or get_object_or_404
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Users,id=id_)

class UsersCreateView(CreateView):
    queryset = Users.objects.all()
    template_name = 'users/users_create.html'
    # Add the form class UsersModelForm
    form_class = UsersModelForm
    # Add the function to check valid_form
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form) #form pass form_class

class UsersUpdateView(UpdateView):
    template_name = 'users/users_create.html'
    form_class = UsersModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Users, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class UsersDeleteView(DeleteView):
    template_name = 'users/users_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Users, id=id_)

    def get_success_url(self):
        return reverse('users:user-list')
