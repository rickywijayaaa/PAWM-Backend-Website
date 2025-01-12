from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('login/', views.login_view),
    #path('../Frontend/html/login.html', views.logout_view, name='logout'),
]
