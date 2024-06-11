from django.db import models
from simple_history.models import HistoricalRecords


class Root(models.Model):
    pass

class Profession(models.Model):
    name = models.CharField(max_length=8)


class Person(Root):
    _history_m2m_fields = ["profession"]
    profession = models.ManyToManyField(Profession, blank=True)
    history = HistoricalRecords()
