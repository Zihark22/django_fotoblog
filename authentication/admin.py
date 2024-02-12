from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin): # we insert these two lines…
    list_display = ('username', 'role') # list the fields we want on the list display

admin.site.register(User, UserAdmin) # we edit this line, adding a second argument