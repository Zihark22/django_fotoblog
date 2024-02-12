from django.contrib import admin
from blog.models import *


class BlogAdmin(admin.ModelAdmin): # we insert these two lines…
    list_display = ('title', 'date_created', 'word_count') # list the fields we want on the list display

admin.site.register(Blog, BlogAdmin) # we edit this line, adding a second argument



class PhotoAdmin(admin.ModelAdmin): # we insert these two lines…
    list_display = ('caption', 'date_created', 'uploader') # list the fields we want on the list display

admin.site.register(Photo, PhotoAdmin) # we edit this line, adding a second argument