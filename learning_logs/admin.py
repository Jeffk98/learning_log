from django.contrib import admin

# Register your models here.

from .models import Topic, Entry

admin.site.register(Topic)  #tells Django to manage our model through the admin site
admin.site.register(Entry)
