from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import TimeInTimeOut
from .forms import TimeInTimeOutForms
from datetime import datetime
from django.contrib import messages

def homepage(request):
    template_name = "app/homepage.html"

    # """ Time In Form """

    now = datetime.now()
    time_now = now.strftime("%H:%M:%S") 
    if request.method=="POST":
        category = request.POST.get('category')
        time_in = time_now
        tito = TimeInTimeOut(category=category, time_in=time_in)
        tito.save()
        messages.error(request, "Time In")
        return redirect("app:homepage")
    else:
        form = TimeInTimeOutForms(request.POST or None)

    # """ Time In List """

    time_in_list = TimeInTimeOut.objects.all().order_by('-time_in')

    context = {
        'form': form,
        'time_in_list' : time_in_list
    }



    return render(request, template_name, context)


def time_out(request, pk):
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    time_data = get_object_or_404(TimeInTimeOut, pk=pk)

    time_data.time_out = time_now
    time_data.save()
    messages.success(request, "Time Out")
    return redirect("app:homepage")
  
def delete(request, pk):

    time_data = get_object_or_404(TimeInTimeOut, pk=pk)

    time_data.delete()
    messages.success(request, "Data successfully deleted")
    return redirect("app:homepage")
  
    