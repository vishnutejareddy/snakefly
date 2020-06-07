from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
]