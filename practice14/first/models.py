from django.db import models

# Create your models here.
class MyModel(models.Model):
    char_field = models.CharField(max_length=255)
    boolean_field = models.BooleanField()
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    integer_field = models.IntegerField()