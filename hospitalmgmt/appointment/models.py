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
    appointmentDate = models.DateTimeField("Next Appointment Time")
    nextRoom = models.CharField("Next Appointed Room", max_length=200, null=True, blank=True)
    class StatusName(models.IntegerChoices):
        OPEN = 0, gtlz("Open")
        CLOSED = 1, gtlz("Closed")
        INPROG = 2, gtlz("In Progress")
        SUSPENDED = 3, gtlz("Suspended")
    # Query with get_FOO_display()
    status = models.IntegerField("Appointment Status",
                              choices=StatusName.choices,
                              default=StatusName.OPEN)
    genderMale = models.BooleanField("Gender is Male", default=True)
    description = models.TextField("Extra Description and Notes",null=True, blank=True)
    # META DATA
    lastUpdatedDate = models.DateTimeField("Last Updated", auto_now=True)
    creationDate = models.DateTimeField("Creation", auto_now_add=True)
    hidden = models.BooleanField("Hide by default", default=False)
    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('app-detail', args=[str(self.id)])
    def get_status(self):
        return self.StatusName.choices
    # Pagination
    class Meta:
        ordering = ['id']
    # TO CHECK IF NULL / NO ENTRY
    # {% if somevar is None %}
