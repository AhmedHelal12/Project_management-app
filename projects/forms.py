
from django import forms
from projects.models import Project
from django.utils.translation import gettext as _
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

        labels = {
            "category" : _("Category"),
            "title" : _("title"),
            "description":_("description")
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
