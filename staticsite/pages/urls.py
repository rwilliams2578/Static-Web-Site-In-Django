from django.urls import path
from .views import Home, Projects, Contact

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("projects/", Projects.as_view(), name="projects"),
    path("contact/", Contact.as_view(), name="contact"),
]
