from django.db import models

# Creo la clase de mis familiares, con herencia de Models
class Familiares(models.Model):
    nombre= models.CharField(max_length=40)
    fecha_nacimiento= models.DateField()
    edad= models.IntegerField() 
    tiene_hijos= models.BooleanField() #True= tiene hijos...
