from django.db import models

# Create your models here.
class sql_db(models.Model):
    img = models.ImageField(upload_to="Photo")
    name = models.CharField(max_length=90)
    desg = models.CharField(max_length=60)
    salary = models.IntegerField()






    9
