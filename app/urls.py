from django.urls import path

from .views import homepage, time_out, delete, category_page, category_delete , SignUpView


app_name = "app"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('time-out/<int:pk>/', time_out, name="time_out"),
    path('delete/<int:pk>/', delete, name="delete"),
    path('category/', category_page, name="category"),
    path('category-delete/<int:pk>/', category_delete, name="category_delete"),
    path('register/', SignUpView.as_view(), name="register"),
]
