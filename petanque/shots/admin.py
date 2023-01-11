from django.contrib import admin
from .models import Player, Judge, Session

# Register your models here.
admin.site.register(Player)
admin.site.register(Judge)
admin.site.register(Session)
