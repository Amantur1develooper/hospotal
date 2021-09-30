from django.db.models.query_utils import subclasses
from django.shortcuts import render,redirect
from .models import Hospital,Doctor, Patients,Nurses
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
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


def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=UserCreationForm()
    return render(request,'addnew.html',{'form':form,})

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    else:
        form=AuthenticationForm()
    return render(request,'addnew.html',{'form':form})

    

def signout(request):
    logout(request)
    return render(request,'index.html')