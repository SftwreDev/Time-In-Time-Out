from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    

class TimeInTimeOut(models.Model):
    
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_in = models.TimeField(auto_now_add=False, blank=True, null=True)
    time_out = models.TimeField(auto_now_add=False,blank=True, null=True)


    def __str__(self):
        return self.category + " | " + f"{self.time_in}" + " | " + f"{self.time_out}"
    