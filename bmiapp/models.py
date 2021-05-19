from django.db import models
from django.contrib.auth.models import User


class Calculator(models.Model):
    
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    height = models.DecimalField(max_digits=5,decimal_places=2)
    bmi = models.DecimalField(max_digits=500,decimal_places=2,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    # def __str__(self):
    #     self.bmi = self.weight/(self.height*self.height)
    #     return str(self.weight)

    # def save(self, *args, **kwargs):
    #     self.bmi = self.weight/(self.height*self.height)
    #     super().save(*args, **kwargs)

    def bmi(self):
        return self.weight/self.height**2


class Suggestion(models.Model):
    ANSWER = (
        ("underweight","UNDERWEIGHT"),
        ("normalweight", "NORMALWEIGHT"),
        ("overweight","OVERWEIGHT"),
        ("obsessed","OBSESSED")
    )
    suggestion = models.CharField(max_length=255, choices=ANSWER)
    result = models.DecimalField(max_digits=500,decimal_places=2)

    def __str__(self):
        return self.suggestion



    









