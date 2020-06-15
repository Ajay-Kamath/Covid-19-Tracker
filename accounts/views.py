from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.contrib.auth.models import User, auth
from .models import Patients
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PatientsForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        age = request.POST['age']
        state = request.POST['slct1']
        city = request.POST['slct2']
        travelhistory = request.POST['travelhistory']
        status = request.POST['slct3']
        patients = Patients(firstname=firstname, lastname=lastname, phonenumber=phone, age=age, state=state, city=city, travelhistory=travelhistory, status=status)
        patients.save();
        print('patient registered')
        return redirect('register')
    else:
        return render(request, 'register.html')

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Patients.objects.filter(Q(firstname__icontains=srch) | Q(city__icontains=srch) | Q(state__icontains=srch) )
            if match:
                return render(request, 'search.html', {'sr':match})
            else:
                messages.error(request,'No result found!')
        else:
            return redirect('search')
    return render(request, 'search.html')

def update(request, pk):
    patient = Patients.objects.get(id=pk)

    form = PatientsForm(instance=patient)

    if request.method == 'POST':
        form = PatientsForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('search')

    context = {'form': form}

    return render(request, 'update.html', context)

def delete(request, pk):
    patient = Patients.objects.get(id=pk)
    patient.delete()
    return redirect('search')

def index(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                # messages.info(request, 'Succesfully logged in!')
                return redirect('register')
        else:
            messages.error(request,'invalid credentials')
            return redirect('index')
    else:
        return render(request, 'index.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def helpfullinks(request):
    return render(request, 'helpfullinks.html')

def logout(request):
    auth.logout(request)
    return redirect('index')