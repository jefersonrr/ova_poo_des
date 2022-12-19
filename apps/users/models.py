from django.db import models

class Person(models.Model):
    cedula = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    type_document = models.CharField(max_length=20,blank=False,null=False)
    phone = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=False,null=False)
    birthdate = models.DateField(blank=True,null=True)
    birthdate_place = models.CharField(max_length=300,null=True, blank=True)
    address = models.CharField(max_length=300,null=True, blank=True)
    codigo = models.CharField(max_length=20,null=True, blank=True)
    def __str__(self):
        return self.name + self.last_name

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=False,null=False)
    descripcion = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    email = models.EmailField(blank=False,null=False)
    password = models.CharField(blank=False, null=False,max_length=20)
    def __str__(self):
        return str(self.id)


    
