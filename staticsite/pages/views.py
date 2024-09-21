from django.views.generic import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = "pages/home.html"


class Projects(TemplateView):
    template_name = "pages/projects.html"


class Contact(TemplateView):
    template_name = "pages/contact.html"
