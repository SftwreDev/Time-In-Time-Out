from django.urls import path

from .views import homepage, time_out, delete


app_name = "app"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('time-out/<int:pk>/', time_out, name="time_out"),
    path('delete/<int:pk>/', delete, name="delete"),
]
