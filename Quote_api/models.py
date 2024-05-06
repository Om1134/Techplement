from django.db import models

# Create your models here.


class Quotes(models.Model):
    quote_id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=50)
    quote_no= models.IntegerField()
    quote = models.TextField()
    author = models.CharField(max_length=30)
    #gender= models.CharField(max_length=10,choices=(('Male','Male',('Female','Female'))))



