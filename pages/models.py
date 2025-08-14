from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100) # first field; in every record, each blog post will have a title
    date = models.DateField()
    content = models.TextField() #when we call models, using the django sublibrary models