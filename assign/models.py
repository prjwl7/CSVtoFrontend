from django.db import models

class Student(models.Model):
    #Primary key
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length = 255, blank = True, null = True)


class address(models.Model):
   student = models.OneToOneField(Student , on_delete = models.CASCADE)
   address_street = models.CharField(max_length=255, blank=True, null=True)
   address_city = models.CharField(max_length=255, blank=True, null=True)
   address_state = models.CharField(max_length=255, blank=True, null=True)
   address_zipcode = models.CharField(max_length=255, blank=True, null=True)

class Hobby(models.Model):
    student = models.OneToOneField(Student , on_delete = models.CASCADE)
    hobby1 = models.CharField(max_length=255, blank=True, null=True)
    hobby2 = models.CharField(max_length=255, blank=True, null=True)
    hobby3 = models.CharField(max_length=255, blank=True, null=True)