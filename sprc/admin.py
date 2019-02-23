from django.contrib import admin

# Register your models here.
from .models import Game
from .models import Post

admin.site.register(Game)
admin.site.register(Post)