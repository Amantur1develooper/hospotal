from django.db.models.query_utils import subclasses
from django.shortcuts import render
from .models import Hospital,Doctor, Patients,Nurses
from django.views.generic import CreateView
from .forms import *
# Create your views here.
def index(request):
    hospitals=Hospital.objects.all()
    return render(request,'index.html',{'hospitals':hospitals}) 

def detail(request,pk):
    hospital_detail=Hospital.objects.get(pk=pk)
    doctor_detail=Doctor.objects.filter(hospital=pk)
    patients_detail=Patients.objects.filter(doctor=pk)
    nurses=Nurses.objects.all()
    patients=Patients.objects.all()
    context={
        'hospital_detail':hospital_detail,
        'doctor_detail':doctor_detail,
        'patients_detail':patients_detail,
        'nurses':nurses,
        'patients':patients
    }
    return render(request, "detail.html", context)

class AddDoctors(CreateView):
    form_class=AddDoctor
    template_name='addnew.html'
    raise_exception=True


class AddNurse(CreateView):
    form_class=AddNurses
    template_name='addnew.html'
    raise_exception=True

class AddPatient(CreateView):
    form_class=AddPatients
    template_name='addnew.html'
    raise_exception=True