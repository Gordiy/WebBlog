from django.urls import path
from viewers import views
from django.contrib.auth.views import login


app_name = 'viewers'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name="profile"),
]
