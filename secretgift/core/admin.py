from django.contrib import admin
from .models import UserSend,AmazonOptions,UserProfile,UserAmazon

# Register your models here.
admin.site.register(UserSend)
admin.site.register(AmazonOptions)
admin.site.register(UserProfile)
admin.site.register(UserAmazon)