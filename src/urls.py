from django.urls import path,include
from django.contrib.auth.views import LoginView

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
    path('financial_report/', views.financial_report, name='financial_report'),
    path('all_projects/', views.our_projects, name="all_projects"),
    path('raise_funds/', views.raise_funds, name="raise_funds"),
    path('contact/', views.contact, name="contact"),
    # path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.redirect_index, name="redirect_index"),
]