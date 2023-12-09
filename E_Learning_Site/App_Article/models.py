from django.db import models
from django.contrib.auth.models import User






# Create your models here.
class Article_post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_articles')
    description = models.TextField(blank=True)
    title = models.CharField(max_length=264,  blank= False)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category=models.CharField(
        max_length=30,
        choices= (('Data Structures', 'Data Structures'),
                 ('Mathematics', 'Mathematics'),
                 ('Information Technology', 'Information Technology'),
                 ('Programming Language', 'Programming Language'),
                 ('Software Development', 'Software Development'),
                 ('Algorithms', 'Algorithms'),
                 ('Artificial Intelligence', 'Artificial Intelligence'),
                 ('Neural Networks', 'Neural Networks'),
                 ('Others', 'Others'),
        )
    )


    class Meta:
        # sort reverse of 'upload date'
        ordering = ('-upload_date',)

    def __str__(self):
        return self.title





class Comment(models.Model):
    article = models.ForeignKey(Article_post, on_delete= models.CASCADE, related_name='article_comment')
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_comment')
    comment=  models.TextField()
    comment_date= models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-comment_date',)  

    def __str__(self):
        return self.comment