from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.CharField(max_length=255, default="Inital Comment......")

    class meta:
        db_table = "note"