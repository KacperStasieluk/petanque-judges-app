from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Session, Player

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('valueEmail').split('@')[0]
        password = request.POST.get('valuePassword')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            request.session['loginFailed'] = False
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(sessions_view)
        else:
            request.session['loginFailed'] = True
            return redirect(login_view)
            # Return an 'invalid login' error message.

    return render(request, 'login.html')

def register_view(request):

    if request.method == 'POST':
        email = request.POST.get('valueEmail')
        username = email.split('@')[0]
        password = request.POST.get('valuePassword')
        repeatPassword = request.POST.get('valueRepeatPassword')

        request.session['registrationFailedPassword'] = False
        request.session['registrationFailedUsername'] = False
        request.session['registrationFailedEmail'] = False

        try:
            validate_email(email)
        except ValidationError as e:
            request.session['registrationFailedEmail'] = True

        if (password != "" and password == repeatPassword):
            if (not (User.objects.filter(username=username).exists())):
                user = User(username=username, email=email, password=password)
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(sessions_view)
            else:
                request.session['registrationFailedUsername'] = True
        else:
            request.session['registrationFailedPassword'] = True

    return render(request, 'register.html')

@login_required
def create_session_view(request):

    players = Player.objects.all()

    if request.method == 'POST':
        nextCode = len(Session.objects.all()) + 1
        players = Player.objects.filter(license_number__in=request.POST.getlist('sessionPlayers'))
        session = Session(code=nextCode, name=request.POST['sessionName'], status='lobby')

        session.save()

        for player in players:
            session.players.add(player)

        return redirect(sessions_view)
    return render(request, 'sessionCreator.html', {'players': players})

@login_required
def sessions_view(request):
    sessions = Session.objects.all()
    #players = session.players.all()
    return render(request, 'sessions.html', {'sessions': sessions})

@login_required
def session_view(request, code):

    session = Session.objects.get(code=code)

    if request.method == 'POST':
        status = request.POST.get('status')

        if (status == 'notJoined'):
            session.judges.add(request.user)
        elif (status == 'lobby'):
            session.status = 'activeEliminations'
            session.save()
        elif (status == 'activeEliminations'):
            pass

    joined = False
    if (request.user in session.judges.all()):
        joined = True

    return render(request, 'sessionView.html', {'session': session, 'joined': joined, 'status': session.status})

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
