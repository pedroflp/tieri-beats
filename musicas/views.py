from django.shortcuts import render
from .forms import HeaderForm, AlertForm, GenreForm, MusicForm, PriceCardForm
from .models import Header, Alert, Genre, Music, PriceCard

# Create your views here.
def index (request):
    header = Header.objects.filter(exibir=True).last()
    return render(request, 'index.html',{'header':header})


def beats (request):
    header = Header.objects.filter(exibir=True).last()
    alert = Alert.objects.filter(exibir=True).last()
    genres = Genre.objects.all()
    musics = Music.objects.all()
    return render(request, 'beats.html',{'header':header, 'alert':alert, 'genres':genres, 'musics': musics})


def freecopyright (request):
    header = Header.objects.filter(exibir=True).last()
    return render(request, 'freecopyright.html',{'header':header})


def pricing (request):
    header = Header.objects.filter(exibir=True).last()
    cards = PriceCard.objects.filter(exibir=True).all()
    return render(request, 'pricing.html',{'header':header, 'cards':cards})


def shop (request):
    header = Header.objects.filter(exibir=True).last()
    musics = Music.objects.all()
    return render(request, 'shop.html',{'header':header, 'musics':musics})

def contact (request):
    header = Header.objects.filter(exibir=True).last()
    return render(request, 'contact.html',{'header':header})

def confirmation (request):
    header = Header.objects.filter(exibir=True).last()
    musics = Music.objects.all()
    cards = PriceCard.objects.filter(exibir=True).all()
    return render(request, 'confirmation.html',{'header':header, 'cards':cards, 'musics':musics})

def checkout (request):
    header = Header.objects.filter(exibir=True).last()
    return render(request, 'checkout.html',{'header':header})