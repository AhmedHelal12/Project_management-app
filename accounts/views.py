from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from accounts.forms import UserRegisterForm
from django.contrib.auth import login
from django.urls import reverse_lazy,reverse
from accounts.forms import UserProfileForm
from django.contrib.auth.models import User

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        login(self.request,self.object)
        return reverse_lazy('project_list')


class UserprofileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'registration/profile.html'
    
    def get_success_url(self):
        return reverse('profile')


    def get_object(self):
        return self.request.user
