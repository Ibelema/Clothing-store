from django.shortcuts import render
from django.views import View
# Create your views here.
class AboutView(view):
    def get(self, request):
        return render(request, "general/about.html")

class ContactView(view):
    def get(self, request):
        return render(request, "general/contact.html")
        