from django.urls import path

from .views import SignUp, edit


urlpatterns = [
    path('profile/', edit, name='profile'),
    path('signup/', SignUp.as_view(), name='signup'),
]