from django import forms
from App_Article.models import Comment




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)