from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_name(request):
    return render(request,template_name="name.html")