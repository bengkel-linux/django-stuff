from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic

# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'index.html', context=context)
