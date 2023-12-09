from django.db import models

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # sort reverse of 'upload date'
        ordering = ('-upload_date',)

    def __str__(self):
        return self.name
    

class Questions(models.Model):
    exam= models.ForeignKey(Exam,on_delete=models.CASCADE, related_name='related_name_of_exam')
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question