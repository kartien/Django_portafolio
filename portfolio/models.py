from hashlib import blake2s
from django.db import models
from django.db.models.fields import CharField, TextField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = TextField(max_length=100)
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)
