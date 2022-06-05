from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myfirst/', views.ChampionListView.as_view(), name='champions')
]
