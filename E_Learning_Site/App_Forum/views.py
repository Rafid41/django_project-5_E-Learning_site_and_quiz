from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
# from App_Article.models import Article_post
from App_Forum.models import Question_post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
#from App_Article.forms import CommentForm
from App_Forum.forms import AnswerForm


# Create your views here.

class QuestionList(ListView):
    context_object_name = 'question_list'  # this 'blog' will be passed to html as dictionary
    model = Question_post
    template_name = 'App_Forum/question_lists.html'


    

class CreateQUestion(LoginRequiredMixin, CreateView):
    model = Question_post
    template_name = 'App_Forum/create_questions.html'
    fields = ('title','description')

 

    #class based view te form submit er por kaj korbe:
    def form_valid(self, form):
        article_obj = form.save(commit=False)
        article_obj.author = self.request.user  # class er kisu use korte hole age "self." add korte hbe
        title = article_obj.title
        article_obj.save()

        return HttpResponseRedirect(reverse('App_Forum:question_lists'))
    


def question_detail(request, pk):
    question = get_object_or_404(Question_post, pk=pk)

    # comment
    answer_form = AnswerForm(request.POST)
    
    if request.method=='POST':
        answer_form = AnswerForm(request.POST)

        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.user = request.user
            answer.question = question   # current ques
            answer.save()

            return HttpResponseRedirect(reverse('App_Forum:question_detail', kwargs={'pk':pk}))
    


    return render(request, 'App_Forum/question_details.html', {'question': question, 'answer_form': answer_form,})