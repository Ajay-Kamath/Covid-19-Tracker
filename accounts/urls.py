from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("index", views.index, name="index"),
    path("logout", views.logout, name="logout"),
    path("search", views.search, name="search"),
    path("faq", views.faq, name="faq"),
    path("about", views.about, name="about"),
    path("helpfullinks", views.helpfullinks, name="helpfullinks"),
    path("update/<str:pk>/", views.update, name="update"),
    path("delete/<str:pk>/", views.delete, name="delete"),
]