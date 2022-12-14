from django.forms import ModelForm,widgets
from . models import project, review
from django import forms
class projectForm(ModelForm):
    class Meta:
        model = project
        fields = ['title', 'description','featured_image','demo_link','source_link','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),

        }
    def __init__(self, *args, **kwargs):
        super(projectForm, self).__init__(*args, **kwargs)
        for name, feild in self.fields.items():
            feild.widget.attrs.update({'class': 'input'})

class reviewForm(ModelForm):
    class Meta:
        model = review  
        fields = ['value','body']     

        label = {
            'value':'place your vote',
            'body': 'add a comment with yur vote'
        }   
    def __init__(self, *args, **kwargs):
        super(reviewForm, self).__init__(*args, **kwargs)
        for name, feild in self.fields.items():
            feild.widget.attrs.update({'class': 'input'})      
            

            