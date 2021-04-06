from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    

class TimeInTimeOut(models.Model):
    status = (
        ('Time In', 'Time In'),
        ('Time Out', 'Time Out'),
        ('Break In', 'Break In'),
        ('Break Out', 'Break Out'),
    )
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shift_date = models.DateField(auto_now_add=False)
    time_in = models.TimeField(auto_now_add=False, blank=True, null=True)
    time_out = models.TimeField(auto_now_add=False,blank=True, null=True)
    break_in = models.TimeField(auto_now_add=False, blank=True, null=True)
    break_out = models.TimeField(auto_now_add=False,blank=True, null=True)
    total_hrs = models.DurationField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    task = models.TextField(max_length=1000, blank=True, null=True)
     

    def __str__(self):
        return f"{self.category}" + " | " + f"{self.time_in}" + " | " + f"{self.time_out}" + " | " + f"{self.shift_date}"
    