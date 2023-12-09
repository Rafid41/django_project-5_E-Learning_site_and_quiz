# from django.db import models
# # from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


# # class UserProfile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
# #     username = models.CharField(max_length=264, blank=True)

# #     account_type = models.CharField(
# #          choices=(('Student', 'Student'),('Teacher', 'Teacher'),)
# #     )


# class User(AbstractUser):
#     account_type = models.CharField(
#         max_length=10,
#         choices=(('Student', 'Student'),('Teacher', 'Teacher'),)
#     )

from django.db import models
from django.contrib.auth.models import AbstractUser,User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='related_name_user')
    account_type = models.CharField(
        max_length=10,
        choices=(('Student', 'Student'),('Teacher', 'Teacher'),)
    )

# class User(AbstractUser):
#     pass  # No need to add the account_type field here