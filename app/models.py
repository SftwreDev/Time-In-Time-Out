from django.db import models

# Create your models here.
class TimeInTimeOut(models.Model):
    cat = (
        ('Quadralogix', 'Quadralogix'),
        ('Getaka Labs', 'Getaka Labs'),
    )
    date_created = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    time_in = models.TimeField(auto_now_add=False, blank=True, null=True)
    time_out = models.TimeField(auto_now_add=False,blank=True, null=True)


    def __str__(self):
        return self.category + " | " + f"{self.time_in}" + " | " + f"{self.time_out}"
    