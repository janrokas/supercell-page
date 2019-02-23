from django.shortcuts import render

# Create your views here.
def brawl(request):
    return render(request, 'game.html', {})