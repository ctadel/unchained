from django.db import models
from datetime import datetime

# Create your models here.
class IP_Records(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    last_updated = models.DateTimeField(default=datetime.now, blank=False)
    last_checked = models.DateTimeField(default=datetime.now, blank=False)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.ip
    

