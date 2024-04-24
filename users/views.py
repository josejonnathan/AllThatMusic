from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import UserCollection, User
from django.urls import reverse_lazy

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    

class UserLoginView(LoginView):
    template_name = 'registration/login.html'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class UserCollectionDetailView(DetailView):
    model = UserCollection
    template_name = 'user_collection_detail.html'

@method_decorator(login_required, name='dispatch')
class UserCollectionCreateView(CreateView):
    model = UserCollection
    fields = ['albums', 'songs', 'artists']
    template_name = 'user_collection_form.html'
    success_url = reverse_lazy('user_collection_detail')
