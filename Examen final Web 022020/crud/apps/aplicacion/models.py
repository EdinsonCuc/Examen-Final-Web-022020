from django.db import models
class tienda(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    lugar=models.CharField(max_length=300)
    telefono=models.CharField(max_length=15)

class articulos(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=20)
    nombreArt=models.CharField(max_length=150)
    descripcion=models.CharField(max_length=150)
    tienda=models.ForeignKey(tienda,on_delete=models.CASCADE)

    


