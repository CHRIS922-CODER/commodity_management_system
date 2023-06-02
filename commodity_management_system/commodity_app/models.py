from django.db import models
from django.core.validators import  MaxValueValidator
from datetime import date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
         return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveBigIntegerField(validators=[MaxValueValidator(999999999)]) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    reorder_level = models.PositiveIntegerField(validators=[MaxValueValidator(9999999)],default=0)
    
    def __str__(self):
        return f"{self.name} {str(self.quantity)}"

class Staff(models.Model):
      name = models.CharField(max_length=50)
      position = models.CharField(max_length=50)
      email= models.CharField(max_length=100)
      phone_number = models.CharField(max_length=10)

      def __str__(self):
           return f"{self.name}  {self.position}"
      
class Department(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
           return f"{self.name}"
      
class Issuance(models.Model):
    quantity_issued = models.PositiveBigIntegerField(validators=[MaxValueValidator(999999999)])
    date_issued = models.DateField(default=date.today)
    status = models.BooleanField(default=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} {self.quantity_issued} {self.department} {self.staff} {self.date_issued}"

      



