from . import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('<str:username>/', views.profile, name="profile"),
]
