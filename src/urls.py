from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('members/', views.members, name='members'),
    path('events/', views.events, name='events'),
    path('read_more/', views.read_more, name='read_more')
]