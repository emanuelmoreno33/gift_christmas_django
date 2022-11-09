from ast import Delete
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField

# Create your models here.

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """
    Model for Profile
    """
    email = models.EmailField(_('Correo electrónico'), unique=True)
    name = models.CharField(max_length=200)
    image = CloudinaryField('image',folder="faces",null = True,blank = True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    datesaved = models.DateTimeField(_('Fecha de registro'),auto_now_add=True)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def __str__(self):
        return self.email

class UserSend(models.Model):
    userFrom = models.ForeignKey(UserProfile,on_delete=models.RESTRICT,related_name="userFrom")
    userTo = models.ForeignKey(UserProfile,on_delete=models.RESTRICT,related_name="userTo")
    emailsend = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

class AmazonOptions(models.Model):
    link = models.URLField(max_length = 1000)
    name =models.TextField(null = True,blank = True)
    imagelink = models.URLField(max_length = 1000,null = True,blank = True)
    price = models.FloatField(null = True,blank = True)


class UserAmazon(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="user")
    amazonOptions = models.ForeignKey(AmazonOptions, on_delete=models.CASCADE)