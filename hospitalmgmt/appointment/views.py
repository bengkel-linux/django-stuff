from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from datetime import datetime, date, time

from .models import Appointment
# Create your views here.

def new_entry(request):
    return render(request, 'new.html', context=context)

def new_post(request):
    return HttpResponseRedirect(reverse('all'))

def update(request, pk):
    if request.method == "POST":
        obj = Appointment.objects.get(id=pk)
        obj.familieName = request.POST['familyname']
        obj.surName = get_none(request.POST['surname'])
        obj.nickName = get_none(request.POST['nickname'])
        obj.caseType = request.POST['case']
        obj.phoneContact = get_none(request.POST['phone'])
        obj.address = get_none(request.POST['address'])
        obj.appointmentDate = to_datetime(request.POST['date'], request.POST['time'])
        obj.nextRoom = request.POST['room'] if request.POST['room'] and request.POST['room'] != "-" else None
        obj.status = request.POST['stats']
        obj.genderMale = request.POST['gender'] == "m"
        obj.hidden = 'hide' in request.POST
        obj.description = get_none(request.POST['desc'])
        obj.save()
    return HttpResponseRedirect(reverse('app-detail', args=[pk]))


class GeneralView(generic.ListView):
    model = Appointment
    paginate_by = 10
    template_name = 'all.html'
    def get_queryset(self):
        return Appointment.objects.filter(hidden=False)
    def get_context_data(self,**kwargs):
        context = super(GeneralView,self).get_context_data(**kwargs)
        context['Verbose'] = False
        return context

class VerboseView(generic.ListView):
    model = Appointment
    paginate_by = 10
    template_name = 'all.html'
    def get_context_data(self,**kwargs):
        context = super(VerboseView,self).get_context_data(**kwargs)
        context['Verbose'] = True
        return context

class DetailView(generic.DetailView):
    model = Appointment
    template_name = 'detail.html'


def get_none(text):
    return text if text else None

def to_datetime(date, time):
    mixed = date+":"+time
    return datetime.strptime(mixed,"%Y-%m-%d:%H:%M")
