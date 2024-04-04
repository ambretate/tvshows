from django.contrib import admin
from .models import TVshow, Viewing, Cast

# Register your models here.
admin.site.register(TVshow)
admin.site.register(Viewing)
admin.site.register(Cast)