from django.urls import path
from  challenge_app import views

app_name = "challenge_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('list/', views.EmailList.as_view(), name="list"),
    path('add/', views.AddEmail.as_view(), name="add")
]
