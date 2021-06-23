from django.contrib import admin
from home.models import Contact

#If there were multiple models than we would have created more registrations.
# Register your models here.
admin.site.register(Contact)


#first we need to register our model in admin.py
#second we need to register our app in the form like home.app.HomeConfig in settings.py of INSTALLED_APPS
#then run the migration command
#migration basically means to generate that file which stores the changes made.
#then run the migrate command which makes the tables in the db
#then write the add content to the db logic which we need to write in view.py
#migrate means apply the pending changes created by makemigrations