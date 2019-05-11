from django.shortcuts import render
from .models import Game
from .models import Post
from .models import Card

# Create your views here.
def home(request):
    games_list = Game.objects.all()
    return render(request, 'home.html', {'games_list': games_list})

def game(request):
    games_list = Game.objects.all()
    gameid = int(request.GET.get('gameid'))
    post_list = Post.objects.filter(game=gameid)
    game = Game.objects.get(id=gameid)
    return render(request, 'game.html', {'games_list': games_list, 'post_list': post_list, 'gameid': gameid, 'game': game})

def maker(request):
    cards_list = Card.objects.all()
    games_list = Game.objects.all()
    return render(request, 'maker.html', {'cards_list': cards_list, 'games_list': games_list})

