# from django import forms 
# from django.contrib.auth.forms import UserCreationForm
# # from App_Login.models import UserProfile
# # from django.contrib.auth.models import User
# from App_Login.models import User


# # account type User class er default field na
# class CreateNewUserForm(UserCreationForm):

#     # account_type = forms.ChoiceField(
#     #     label='Account Type',
#     #     choices=UserProfile.account_type,
#     #     widget=forms.Select(attrs={'class': 'form-control', })
#     # )

#     account_type = forms.CharField(
#         label='Account Type',
#     )
#     username = forms.CharField(
#         required=True, 
#         label="Username", 
#         widget=forms.TextInput()
#     )
#     password1 = forms.CharField(
#         required=True,
#         label='Password',
#         widget = forms.PasswordInput(),
#     )
#     password2 = forms.CharField(
#         required=True,
#         label='Confirm Password',
#         widget = forms.PasswordInput(),
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'account_type', 'password1', 'password2')
#         # widgets = {
#         #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username','label':''}),
#         #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
#         #     'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#         # }

#     # def save(self, commit=True):
#     #     user_profile = super().save(commit=False)
#     #     user_profile.user.set_password(self.cleaned_data['password1'])

#     #     if commit:
#     #         user_profile.save()

#     #     return user_profile
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from App_Login.models import UserProfile
from App_Login.models import User

class CreateNewUserForm(UserCreationForm):

    account_type = forms.ChoiceField(
        label='Account Type',
        choices=UserProfile._meta.get_field('account_type').choices,
        widget=forms.Select(attrs={'class': 'form-control', })
    )

    username = forms.CharField(required=True, label="username", widget=forms.TextInput())
    password1 = forms.CharField(
        required=True,
        label='Password',
        widget = forms.PasswordInput(),
    )
    password2 = forms.CharField(
        required=True,
        label='Confirm Password',
        widget = forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ('username', 'account_type', 'password1', 'password2')

        # labels = {
        #     'username': 'Username',
        #     'password1': 'Password',
        #     'password2': 'Confirm Password',
        # }
       
