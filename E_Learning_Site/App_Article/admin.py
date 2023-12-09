from django.contrib import admin
from App_Article.models import Article_post, Comment

# Register your models here.
admin.site.register(Article_post)
admin.site.register(Comment)
