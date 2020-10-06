from django.contrib import admin
from .models import Header, Alert, Genre, Music, PriceCard


# Register your models here.
admin.site.register(Header)
admin.site.register(Alert)
admin.site.register(Genre)
admin.site.register(Music)
admin.site.register(PriceCard)