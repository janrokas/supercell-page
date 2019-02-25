from django.shortcuts import render
from .models import Game
from .models import Post

# Create your views here.
def home(request):
    games_list = Game.objects.all()
    return render(request, 'home.html', {'games_list': games_list})

def game(request):
    games_list = Game.objects.all()
    gameid = int(request.GET.get('gameid'))
    post_list = Post.objects.filter(game=gameid)
    return render(request, 'game.html', {'games_list': games_list, 'post_list': post_list, 'gameid': gameid})
