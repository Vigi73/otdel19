from django import forms
from .models import Post_guest

class PostForm(forms.ModelForm):

    class Meta:
        model = Post_guest
        fields = ('g_title', 'g_text')