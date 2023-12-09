from django import forms
from App_Forum.models import Answers




class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('answer',)