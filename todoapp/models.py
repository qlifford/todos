from django.db import models

# Create your models here.
class Todolist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
