from django.conf import settings
from django.db import models
from django.utils import timezone

class whitelist(models.Model):
    name_wl = models.CharField(max_length=200)
    photo_wl = models.CharField(max_length=200)
    status_wl = models.BooleanField()

    def __str__(self):
        return self.name_wl

class blacklist(models.Model):
    name_bl = models.CharField(max_length=200)
    photo_bl = models.CharField(max_length=200)

    def __str__(self):
        return self.name_bl

class whitelist_stat(models.Model):
    person = models.ForeignKey('whitelist', on_delete=models.DO_NOTHING)
    date_in = models.DateField()
    time_in = models.TimeField()
    date_out = models.DateField(null=True)
    time_out = models.TimeField(null=True)

    def person_in(self):
        self.date_in = timezone.now()
        self.time_in = timezone.now()
        self.save()

    def person_out(self):
        self.date_out = timezone.now()
        self.time_out = timezone,now()
        self.save()

    def __str__(self):
        return str(self.person)
    

