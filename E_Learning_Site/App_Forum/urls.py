from django.urls import path
from App_Forum import views



app_name = "App_Forum"

urlpatterns = [
    path('', views.QuestionList.as_view(), name='question_lists'),
    path('create_question', views.CreateQUestion.as_view(), name='create_question'),
    path('question_detail/<pk>/', views.question_detail, name="question_detail"),
]