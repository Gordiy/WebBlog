from django.urls import path
from wall import views


urlpatterns = [
    path('wall/', views.wall_information, name='wall_information'),
]
