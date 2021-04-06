from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import TimeInTimeOut, Category
from .forms import TimeInTimeOutForms, CategoryForms
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
import speech_recognition as sr
import pyttsx3 

r = sr.Recognizer() 



@login_required
def homepage(request):
    template_name = "app/homepage.html"
    
    # """ Time In Form """
    form = TimeInTimeOutForms(request.POST or None)
    now = datetime.now()
    date_today = now.strftime("%B %d %Y") 
    time_now = now.strftime("%H:%M:%S") 

    if form.is_valid():
        
        form.save()
        messages.error(request, "Schedule Created")
        text = r.listen("Schedule created")
        
        return redirect("app:homepage")
    else:
        form = TimeInTimeOutForms(request.POST or None)

    # """ Time In List """
    date_today = now.strftime("%B %d %Y") 
    print(date_today)
    time_in_list = TimeInTimeOut.objects.filter(shift_date=now).order_by('shift_date')

    context = {
        'form': form,
        'time_in_list' : time_in_list,
        'date_today' : date_today,
    }
    return render(request, template_name, context)

@login_required
def schedule_page(request):
    template_name = "app/schedule_page.html"

    # """ Time In Form """
    form = TimeInTimeOutForms(request.POST or None)
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S") 
    if form.is_valid():
        
        form.save()
        messages.error(request, "Schedule Created")
        text = "Schedule Created"
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text) 
        engine.runAndWait()
        return redirect("app:schedule_page")
    else:
        form = TimeInTimeOutForms(request.POST or None)

    # """ Time In List """
    date_today = now.strftime("%B %d %Y") 
    print(date_today)
    time_in_list = TimeInTimeOut.objects.all().order_by('shift_date')

    context = {
        'form': form,
        'time_in_list' : time_in_list,
        'date_today' : date_today,
    }
    return render(request, template_name, context)

@login_required
def time_out(request, pk):
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    time_data = get_object_or_404(TimeInTimeOut, pk=pk)
    
    time_in_list = TimeInTimeOut.objects.all().order_by('-time_in')

    for i in time_in_list:

        date = i.date_created
        in_time = datetime.combine(date, i.time_in)
        total = now - in_time

    total_time = total
    print("Total",total_time)
    time_data.total_hrs = total_time
    time_data.time_out = time_now
    time_data.status = "Time Out"
    text = "Time Out"
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text) 
    engine.runAndWait()
    time_data.save()
    messages.success(request, "Time Out")
    return redirect("app:homepage")

@login_required
def break_out(request, pk):
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    time_data = get_object_or_404(TimeInTimeOut, pk=pk)
    
    time_data.break_out = time_now
    time_data.status = 'Break Out'
    text = "Break Out"
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text) 
    engine.runAndWait()
    time_data.save()
    messages.success(request, "On-Break")
    return redirect("app:homepage")

@login_required
def time_in(request, pk):
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    time_data = get_object_or_404(TimeInTimeOut, pk=pk)
    text = "Time In"
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text) 
    engine.runAndWait()
    time_data.time_in = time_now
    time_data.status = 'Time In'
    time_data.save()
    messages.success(request, "Time In")
    return redirect("app:homepage")

@login_required
def break_in(request, pk):
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    time_data = get_object_or_404(TimeInTimeOut, pk=pk)
    
    time_data.break_in = time_now
    time_data.status = "Break In"
    text = "Break In"
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text) 
    engine.runAndWait()
    time_data.save()
    messages.success(request, "Break In")
    return redirect("app:homepage")

@login_required
def delete(request, pk):

    time_data = get_object_or_404(TimeInTimeOut, pk=pk)

    time_data.delete()
    messages.success(request, "Data successfully deleted")
    text = "Data successfully deleted"
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text) 
    engine.runAndWait()
    return redirect("app:schedule_page")
  

@login_required
def category_page(request):
    template_name = "app/category.html"

    category = Category.objects.all()

    form = CategoryForms(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Category created successfully")
        return redirect("app:category")
    else:
        form = CategoryForms(request.POST or None)

    context = {
        "category" : category,
        'form' : form
    }

    return render(request, template_name, context)

@login_required   
def category_delete(request, pk):

    category = get_object_or_404(Category, pk=pk)

    category.delete()
    messages.success(request, "Data successfully deleted")
    return redirect("app:category")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'