from django.urls import path
from App_Article import views



app_name = "App_Article"

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_lists'),
    path('create_article', views.CreateArticle.as_view(), name='create_article'),
    path('article_detail/<pk>/', views.article_detail, name="article_detail"),
]