from cProfile import label
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','password1','password2']
        labels = {
            'first_name': 'Name',
        }
    def __init__(self, *args, **kwargs):
        super(customUserCreationForm, self).__init__(*args, **kwargs)
        for name, feild in self.fields.items():
            feild.widget.attrs.update({'class': 'input'})   
             
      

class Profileform(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'location', 'bio', 'short_intro', 'profile_image',
                  'social_github', 'social_linkedin', 'social_twitter',
                  ]

    def __init__(self, *args, **kwargs):
        super(Profileform, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})           