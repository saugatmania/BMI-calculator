from django.db import models
from django.contrib.auth.models import User


class Calculator(models.Model):
    
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    height = models.DecimalField(max_digits=5,decimal_places=2)
    bmi = models.DecimalField(max_digits=5,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name="calculator", on_delete=models.CASCADE, null=True)


    def bmi(self):
        return self.weight/self.height**2
        
    def __str__(self):
        return str(self.weight)






    









