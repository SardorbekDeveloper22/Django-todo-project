from django.db import models
from django.urls import reverse

# Create your models here.
class ToDo(models.Model):
    class Status(models.TextChoices):
        Progress = "PR", "In Progress"
        Done = "DN", "Done"
        Incomplete = 'NO', 'Incomplete'
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.Progress )

    def get_absolute_url(self):
        return reverse("home")
