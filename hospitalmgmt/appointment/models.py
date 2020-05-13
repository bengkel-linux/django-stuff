from django.db import models
from django.utils.translation import gettext_lazy as gtlz
from django.urls import reverse


class Appointment(models.Model):
    caseType = models.CharField("AnimuName Kanji", max_length=200, default="")
    phoneContact = models.CharField("Phone Number", max_length=200, null=True, blank=True)
    address = models.CharField("Address", max_length=200, null=True, blank=True)
    appointmentDate = models.DateTimeField("Last Updated")
    lastUpdatedDate = models.DateTimeField("Last Updated", auto_now=True)
    creationDate = models.DateTimeField("Creation", auto_now_add=True)
