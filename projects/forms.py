
from django import forms
from projects.models import Project

class ProjectCreateForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title','description','category']
        widgets = {
            "title": forms.TextInput(),
            "description": forms.Textarea(),
            "category" : forms.Select()

        }

        
class ProjectUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title','category','status']
        widgets = {
            "title": forms.TextInput(),
            "description": forms.Textarea(),
            "status" : forms.Select()

        }
