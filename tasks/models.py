from django.db import models

# Create your models here.


class Task(models.Model):
    level_choices = [
        ('i','important'),
        ('u', 'unimportant')
    ]
    title = models.CharField(max_length=20)
    complete = models.BooleanField()
    level = models.CharField(choices=level_choices, max_length=1,default='u')
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.title