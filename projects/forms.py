from .models import ProjectPost
from core.forms import BaseForm
from django import forms

class ProjectForm(BaseForm):

    class Meta:
        model = ProjectPost
        fields = BaseForm.Meta.fields + ["topic","maincontent"]
        widgets = {
            'thumbnail': forms.ClearableFileInput(attrs={'onchange': 'PreviewImage()'})
        }

