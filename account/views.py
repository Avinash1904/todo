from django.urls import reverse_lazy
from django.views import generic

from account.forms import SignupForm
from .models import User

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"