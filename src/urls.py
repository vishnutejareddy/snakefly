from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('members/', views.members, name='members'),
    path('events/', views.events, name='events'),
    path('read_more/', views.read_more, name='read_more'),
    path('events/<int:id>', views.read_event, name='read_event'),
    path('volunter/', views.volunter, name='volunter'),
    path('volunter/<int:id>', views.read_volunter_event, name='read_volunter_event'),
]