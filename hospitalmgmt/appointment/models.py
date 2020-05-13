from django.db import models
from django.utils.translation import gettext_lazy as gtlz
from django.urls import reverse


class Appointment(models.Model):
    familieName = models.CharField("Family", max_length=200, default="")
    surName = models.CharField("Surname", max_length=200, null=True, blank=True)
    nickName = models.CharField("Nickname", max_length=200, null=True, blank=True)
    caseType = models.CharField("Type of Case", max_length=200, default="")
    phoneContact = models.CharField("Phone Number", max_length=200, null=True, blank=True)
    address = models.CharField("Address", max_length=200, null=True, blank=True)
    appointmentDate = models.DateTimeField("Last Updated")
    class StatusName(models.TextChoices):
        OPEN = "O", gtlz("Open")
        CLOSED = "C", gtlz("Closed")
        INPROG = "I", gtlz("In Progress")
        SUSPENDED = "P", gtlz("Suspended")
    status = models.CharField("Appointment Status",
                              max_length=1,
                              choices=StatusName.choices,
                              default=StatusName.OPEN)
    # META DATA
    lastUpdatedDate = models.DateTimeField("Last Updated", auto_now=True)
    creationDate = models.DateTimeField("Creation", auto_now_add=True)
