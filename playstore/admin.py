from django.contrib import admin
from .models import App, Device, Game, Book, Movie
# Register your models here.

admin.site.register(App)
admin.site.register(Device)
admin.site.register(Game)
admin.site.register(Book)
admin.site.register(Movie)
