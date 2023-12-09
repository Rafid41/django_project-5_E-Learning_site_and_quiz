from django.db import models
from django.contrib.auth.models import User






# Create your models here.
class Question_post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_questions')
    description = models.TextField(blank=True)
    title = models.CharField(max_length=264,  blank= False)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)



    class Meta:
        # sort reverse of 'upload date'
        ordering = ('-upload_date',)

    def __str__(self):
        return self.title





class Answers(models.Model):
    question = models.ForeignKey(Question_post, on_delete= models.CASCADE, related_name='question_answers')
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_aswer')
    answer=  models.TextField()
    answer_date= models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-answer_date',)  

    def __str__(self):
        return self.answer