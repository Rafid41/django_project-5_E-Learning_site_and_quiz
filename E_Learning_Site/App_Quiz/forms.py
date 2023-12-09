from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 

 
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question', 'op1', 'op2', 'op3', 'op4', 'ans']