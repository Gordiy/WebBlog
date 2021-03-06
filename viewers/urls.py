from django.urls import path
from viewers import views
from django.contrib.auth.views import login


app_name = 'viewers'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name="profile"),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('additional_inform/<username>/', views.additional_inform, name='additional_inform'),
    # path('profile_photo/<username>/', views.profile_photo, name='user_profile_photo')
]
