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
