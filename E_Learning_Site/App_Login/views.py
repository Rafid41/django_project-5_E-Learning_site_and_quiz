from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from App_Login.models import UserProfile

from django.urls import reverse
from App_Login.forms import CreateNewUserForm

def sign_up(request):
    # form = CreateNewUserForm()

    # if request.method == 'POST':
    #     form = CreateNewUserForm(request.POST)
    #     if form.is_valid():
    #         user_profile = form.save(commit=False)
    #         user_profile.user = form.instance
    #         user_profile.save()
    form = CreateNewUserForm()
    registered = False

    if request.method == 'POST':
        form = CreateNewUserForm(data = request.POST)

        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile.objects.create(user=user, account_type=form.cleaned_data['account_type'])
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))   

            # login(request, form.instance)
            #return HttpResponseRedirect(reverse('App_Login:login'))

    return render(request, 'App_Login/signup.html', context={'form': form})



def login_page(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form= AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username =username, password = password)

            # user account active kina check
            if user is not None:
                login(request, user)
                print(user.related_name_user.account_type)
                return HttpResponseRedirect(reverse('App_Article:article_lists'))

    return render(request, 'App_Login/login.html',context= {'form':form})
        


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))