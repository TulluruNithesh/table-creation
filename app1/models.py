from django.db import models

# Create your models here.
class Table(models.Model):
    emp_lastname=models.CharField(max_length=100)
    emp_firstname=models.CharField(max_length=100)
    emp_address=models.CharField(max_length=100)
    emp_city=models.CharField(max_length=100)

    def __str__(self):
        return self.emp_lastname




