from django.shortcuts import render, redirect, HttpResponse
from .models import User, Appointment
import bcrypt, time
from datetime import datetime, date
from django.contrib import messages
def index(request):

    return render(request, 'main/index.html')

def success(request):
    appointments = Appointment.objects.all().order_by('date')


    context = {
    'appointments': appointments,
    'datetime': datetime.now(),
    'date': datetime.date(datetime.now())
    }
    return render(request, 'main/success.html', context)

def create(request):
    if User.objects.registration(request.POST):

        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
    else:
        messages.error(request, "Registration Error")

    return redirect('/')

def login(request):
    if User.objects.login(request.POST):
        identify = User.objects.get(email=request.POST['email_login'])
        request.session['id'] = identify.id
        request.session['first_name'] = identify.first_name
        return redirect('/success')
    else:
        messages.error(request, "Login Error")
        return redirect('/')

def new_app(request):
    if request.POST['app_date'] < str(datetime.date(datetime.now())):
        messages.error(request, "Predate Error")
        return redirect('/success')

    else:
        Appointment.objects.create(date=request.POST['app_date'], time=request.POST['app_time'], status="Pending", task=request.POST['app_task'], user_id=User.objects.get(id = request.session['id']))
        return redirect('/success')

def update_page(request, id):
    appointments = Appointment.objects.get(id=id)

    context = {
    'appointments': appointments
    }
    return render(request, 'main/appointments.html', context)

def update(request, id):
    if request.POST['app_date_edit'] < str(datetime.date(datetime.now())):
        messages.error(request, "Predate Error")
        return redirect('/success')
    else:
        Appointment.objects.create(date=request.POST['app_date_edit'], time=request.POST['app_time_edit'], status=request.POST['app_status_edit'], task=request.POST['app_task_edit'], user_id=User.objects.get(id = request.session['id']))
        Appointment.objects.get(id=id).delete()
        return redirect('/success')

def delete(request, id):
    # Appointment.objects.all(),
    Appointment.objects.get(id = id).delete()
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')
