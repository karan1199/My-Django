from django.contrib import admin
from django.urls import path
from website import views




urlpatterns = [
    path("",views.index ,name="index"),
    path("about",views.about ,name="about"),
    path("skills",views.skills ,name="skills"),
    path("projects",views.projects ,name="projects"),
    path("contact",views.contact ,name="contact")
       
] 