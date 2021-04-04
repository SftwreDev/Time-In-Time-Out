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


@login_required
def homepage(request):
    template_name = "app/homepage.html"

    # """ Time In Form """
    form = TimeInTimeOutForms(request.POST or None)
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S") 
    if form.is_valid():
        tito = form.save(commit=False)
        tito.time_in = time_now
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

@login_required
def time_out(request, pk):
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    time_data = get_object_or_404(TimeInTimeOut, pk=pk)

    time_data.time_out = time_now
    time_data.save()
    messages.success(request, "Time Out")
    return redirect("app:homepage")

@login_required
def delete(request, pk):

    time_data = get_object_or_404(TimeInTimeOut, pk=pk)

    time_data.delete()
    messages.success(request, "Data successfully deleted")
    return redirect("app:homepage")
  

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