from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Appointment
# Create your views here.

def new_entry(request):
    return render(request, 'new.html', context=context)

class GeneralView(generic.ListView):
    model = Appointment
    paginate_by = 10
    template_name = 'all.html'

class DetailView(generic.DetailView):
    model = Appointment
    template_name = 'detail.html'
