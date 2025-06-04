from django.db import models


# Create your models here.
class People(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    sports = models.CharField(max_length=100)

    class Meta:
        db_table = 'People'

#  git init
#