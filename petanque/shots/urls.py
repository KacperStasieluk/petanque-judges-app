from django.urls import path
from .views import login_view, register_view, create_session_view, session_view, ranking_view, semifinals_view, finals_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('create_session/', create_session_view, name='create_session'),
    path('session/<str:code>/', session_view, name='session'),
    path('ranking/', ranking_view, name='ranking'),
    path('semifinals/', semifinals_view, name='semifinals'),
    path('finals/', finals_view, name='finals'),
]
