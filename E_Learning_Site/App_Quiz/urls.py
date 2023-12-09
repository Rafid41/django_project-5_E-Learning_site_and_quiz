from django.urls import path
from .views import create_exam,create_exam, add_question,view_exam,ExamList, take_exam

app_name = 'App_Quiz'


urlpatterns = [
    path('create/', create_exam, name='create_exam'),
    path('add_question/<int:exam_id>/', add_question, name='add_question'),
    path('take_exam/<pk>/', take_exam, name='take_exam'),
    path('exam_list/',ExamList.as_view(), name='exam_list'),
]
