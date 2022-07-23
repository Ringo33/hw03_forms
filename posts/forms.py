from django import forms
from django.forms import ModelForm
from .models import Post, Book, Comment

# GROUPS = (
#     ("Botanics", "Botanics"),
#     ("Pilots", "Pilots"),
#     ("Students", "Students"),
# )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['group', 'text', 'image']

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, help_text='Добавьте комментарий к посту')
    class Meta:
        model = Comment
        fields = ['text']


# class PostForm(forms.Form):
#     group = forms.ChoiceField(choices=GROUPS, required = False)
#     text = forms.CharField(widget=forms.Textarea, required = True)

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['text']