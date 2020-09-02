# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class User(AbstractBaseUser):
    """
    Store User account details.
    """
    
    name = models.CharField('name', max_length=80, null=True, blank=True)
    email = models.EmailField('email address', unique=False, null=True, blank=True)
    phone_number = models.CharField('Phone Number', unique=False, max_length=90, null=False, blank=False)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'
        ordering = ['name', ]

    def __str__(self):
        return '<{id}>: {email}'.format(
            id=self.id,
            email=self.email,
        )


class UserContact(models.Model):
    """
    MovieDetail model used to save the Movie details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_contact')
    name = models.CharField('name', max_length=80, null=True, blank=True)
    email = models.EmailField('email address', unique=False, null=True, blank=True)
    phone_number = models.CharField('Phone Number', unique=False, max_length=80, null=False, blank=False)
    is_spam = models.BooleanField('Is Spam', default=False)

    class Meta:
        verbose_name = "user_contact"

    def __str__(self):
        return self.name



