from django.db import models

class DataFile(models.Model):
    file = models.FileField(upload_to='data/')
