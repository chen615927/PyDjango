from django.db import models

class Publisher(models.Model):
  name = models.CharField(max_length = 30)
  address = models.CharField(max_length = 100)
  city = models.CharField(max_length = 20)
  telphone = models.CharField(max_length = 13)
  gmt_create = models.DateField()

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']

  class Admin:
    pass
