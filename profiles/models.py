from distutils.command.upload import upload
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name,  password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    picture = models.ImageField( upload_to= 'profile_pics', blank=True, null = True)
    user_name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    rank = models.CharField(max_length=150, blank=True)
    mobile_1 = models.CharField(max_length=150)
    mobile_2 = models.CharField(max_length=150, blank=True, null= True)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name