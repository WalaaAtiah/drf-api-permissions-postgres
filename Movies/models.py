from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class  Move(models.Model):
    Genre=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Genre

class Drama(models.Model):
    name=models.CharField(max_length=255)
    publisher=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Genre=models.ForeignKey(Move(),on_delete=models.CASCADE)
    global_assessment=models.CharField(max_length=255)
    duration=models.IntegerField()
    
    def __str__(self):
        return self.name

class Action(models.Model):
    name=models.CharField(max_length=255)
    publisher=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Genre=models.ForeignKey(Move(),on_delete=models.CASCADE)
    global_assessment=models.CharField(max_length=255)
    duration=models.IntegerField()
    
    def __str__(self):
        return self.name

class Animation(models.Model):
    name=models.CharField(max_length=255)
    publisher=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Genre=models.ForeignKey(Move(),on_delete=models.CASCADE)
    global_assessment=models.CharField(max_length=255)
    duration=models.IntegerField()
    
    def __str__(self):
        return self.name