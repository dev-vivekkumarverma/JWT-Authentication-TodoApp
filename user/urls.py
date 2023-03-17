from django.urls import path,include
from .views import LogInView,RegistrationView
urlpatterns = [
    path('login/',LogInView.as_view()),
    path('register/',RegistrationView.as_view()),
]
