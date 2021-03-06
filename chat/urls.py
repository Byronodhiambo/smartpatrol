
from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [

    path('', views.index, name='index'),
    path('get/', views.get, name='get'),
    path('history/<str:room_id>/', views.history, name='history'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('<str:group_id>/', views.room, name='room'),
    path('help/', views.help, name='help'),
    path('report/', views.report, name='report'),
]
