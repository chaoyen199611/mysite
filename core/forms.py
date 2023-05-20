from django.forms import ModelForm
from django import forms
from .models import PostBase
from blog.models import BlogPost

class BaseForm(ModelForm):

    topic = forms.CharField()
    just_test = forms.CharField()
    
    class Meta:
        model = PostBase
        fields = ["title","category","description","thumbnail"]
        widgets = {
            'thumbnail': forms.ClearableFileInput(attrs={'onchange': 'PreviewImage()'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"] = forms.CharField(widget=forms.Textarea)
        self.fields['category'].choices = [
            ('Blog', 'Blog'),
            ('Photo', 'Photo'),
            ('Travel', 'Travel'),
            ('Review', 'Review'),
            ('Project', 'Project'),
        ]
