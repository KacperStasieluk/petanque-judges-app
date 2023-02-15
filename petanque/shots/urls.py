from django.urls import path
from .views import login_view, register_view, create_session_view, sessions_view, session_view, ranking_view, semifinals_view, finals_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('sessionCreator/', create_session_view, name='sessionCreator'),
    path('sessions/', sessions_view, name='sessions'),
    path('session/<int:code>/', session_view, name='sessionView'),
    path('ranking/', ranking_view, name='ranking'),
    path('semifinals/', semifinals_view, name='semifinals'),
    path('finals/', finals_view, name='finals'),
]
