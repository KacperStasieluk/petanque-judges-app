from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Session, Player

def login_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # rejestracja użytkownika
            pass
    return render(request, 'Petanque/register.html', {'form': form})

@login_required
def create_session_view(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            # tworzenie nowej sesji
            pass
    return render(request, 'Petanque/create_session.html', {'form': form})

@login_required
def session_view(request, code):
    session = Session.objects.get(code=code)
    players = session.players.all()
    return render(request, 'Petanque/session.html', {'session': session, 'players': players})

@login_required
def ranking_view(request):
    players = Player.objects.all()
    # obliczenie rankingu zawodników
    return render(request, 'Petanque/ranking.html', {'players': players})

@login_required
def semifinals_view(request):
    players = Player.objects.filter(status='semifinalist')
    # przeprowadzanie rozgrywek półfinałowych
    return render(request, 'Petanque/semifinals.html', {'players': players})

@login_required
def finals_view(request):
    players = Player.objects.filter(status='finalist')
    # przeprowadzanie rozgrywek finałowych
    return render(request, 'Petanque/finals.html', {'players': players})
