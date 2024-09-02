
from django import forms
from projects.models import Project

attrs={'class':'form-control','style':'margin: 10px;'}

class ProjectCreateForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title','description','category']
        widgets = {
            "category" : forms.Select(attrs=attrs),
            "title": forms.TextInput(attrs=attrs),
            "description": forms.Textarea(attrs=attrs),
        }

        
class ProjectUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title','status','category']
        widgets = {
            "category": forms.Select(attrs=attrs),
            "title": forms.TextInput(attrs=attrs),
            "status" : forms.Select(attrs=attrs)

        }
