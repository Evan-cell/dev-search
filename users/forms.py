from cProfile import label
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','password1','password2']
        labels = {
            'first_name': 'Name',
        }