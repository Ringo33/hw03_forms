from django import forms
from django.forms import ModelForm
from .models import Post, Book

# GROUPS = (
#     ("Botanics", "Botanics"),
#     ("Pilots", "Pilots"),
#     ("Students", "Students"),
# )


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['group', 'text']

# class PostForm(forms.Form):
#     group = forms.ChoiceField(choices=GROUPS, required = False)
#     text = forms.CharField(widget=forms.Textarea, required = True)

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['text']