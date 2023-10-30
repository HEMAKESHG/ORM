# Ex02 Django ORM Web Application
## Date: 18.10.23

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import football_players,football_playersAdmin
admin.site.register(football_players,football_playersAdmin)

models.py
from django.db import models
from django.contrib import admin
class football_players(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    mobile_number=models.IntegerField()
    jersey_number=models.IntegerField()
    achievements=models.CharField(max_length=200)
    height=models.IntegerField()
    weight=models.IntegerField()

class football_playersAdmin(admin.ModelAdmin):
    list_display=["name","age","mobile_number","jersey_number","achievements","height","weight"]
```

## OUTPUT
![image](https://github.com/HEMAKESHG/ORM/assets/144870552/04eae038-0696-4880-8f5d-d95238fdcd58)
## RESULT
Thus the program for creating a database using ORM hass been executed successfully
