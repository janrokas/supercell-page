from django.contrib import admin

# Register your models here.
from .models import Game
from .models import Post
from .models import Card

admin.site.register(Game)
admin.site.register(Post)
admin.site.register(Card)