from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    def get(self, request):
        return render(request, template_name='rsvp/index.html')