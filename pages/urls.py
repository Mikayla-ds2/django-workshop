from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("<int:pk>", views.detail, name='detail') #pass along the number = primary key for each blog post in the url
    ]