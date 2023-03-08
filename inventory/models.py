from django.db import models

# Create your models here.
class Catigories(models.Model):
  # name = models.
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  pass


class Product(models.Model):
  # catigorie = models.ForeignKey(Catigories, null=True, blank=True, on_delete=models.SET_NULL)
  catigorie = models.ManyToManyField('Tag', blank=True)
  # name =
  pass