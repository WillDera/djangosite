from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = models.Article
        fields = ('title','slug','body','thumb')
