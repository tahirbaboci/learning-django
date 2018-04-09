from django.db import models

# Create your models here.

class Employee(models.Model):
    nome = models.CharField(max_length=250)
    email = models.CharField(max_length=500)

    def __str__(self):
        return "name : " + self.nome + "\nemail : " + self.email

