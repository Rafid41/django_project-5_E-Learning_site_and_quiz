from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Article.models import Article_post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from App_Article.forms import CommentForm


# Create your views here.

class ArticleList(ListView):
    context_object_name = 'article_list'  # this 'blog' will be passed to html as dictionary
    model = Article_post
    template_name = 'App_Article/article_lists.html'


    

class CreateArticle(LoginRequiredMixin, CreateView):
    model = Article_post
    template_name = 'App_Article/create_article.html'
    fields = ('title','category','description')

 

    #class based view te form submit er por kaj korbe:
    def form_valid(self, form):
        article_obj = form.save(commit=False)
        article_obj.author = self.request.user  # class er kisu use korte hole age "self." add korte hbe
        title = article_obj.title
        article_obj.save()

        return HttpResponseRedirect(reverse('App_Article:article_lists'))
    


def article_detail(request, pk):
    article = get_object_or_404(Article_post, pk=pk)

    # comment
    comment_form = CommentForm(request.POST)
    
    if request.method=='POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article = article   # current video
            comment.save()

            return HttpResponseRedirect(reverse('App_Article:article_detail', kwargs={'pk':pk}))
    


    return render(request, 'App_Article/article_details.html', {'article': article, 'comment_form': comment_form,})