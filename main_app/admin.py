from django.contrib import admin
from .models import Craft, Favorite, Photo, Badge, Spacecraft

# Register your models here.
admin.site.register(Craft)
admin.site.register(Favorite)
admin.site.register(Photo)
admin.site.register(Badge)
admin.site.register(Spacecraft)
