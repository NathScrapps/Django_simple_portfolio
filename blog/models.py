import datetime
from django.db import models
from django.db.models.base import Model
import datetime

# Create your models here.
class Post(models.Model):
    # Import type vars; second form
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images/")
    date = models.DateField(datetime.date.today)



# Import type vars; first form
# from django.db.models.fields import CharField, URLField
# from django.db.models.fields.files import ImageField
# class Post(models.Model):
#     title = CharField(max_length=100)
#     description = CharField(max_length=250)
#     image = ImageField(upload_to="portfolio/images/")
#     date = URLField(blank=True)
