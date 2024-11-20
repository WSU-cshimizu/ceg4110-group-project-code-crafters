from django.db import models
from userAccounts.models import *
import string, secrets


def modalID_generator():
    alphabet = string.ascii_letters
    modalID = ''.join(secrets.choice(alphabet) for i in range(10))
    return modalID


class votingschedule(models.Model):
    department = models.TextField(choices=(
        ('CECS','CECS'),
        ('CSM','CSM'),
        ('CLA','CLA'),
        ('CBUS','CBUS'),
        ), null=True)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.department}"
    
    class Meta:
        verbose_name = "Voting Schedules"  
        verbose_name_plural = "Voting Schedules"


class UserRecords(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    president = models.CharField(max_length=50, blank=True, null=True)
    vice_president = models.CharField(max_length=50, blank=True, null=True)
    treasurer = models.CharField(max_length=50, blank=True, null=True)
    secretary = models.CharField(max_length=50, blank=True, null=True)
    event_coordinator = models.CharField(max_length=50, blank=True, null=True)
    sports_recreation_officer = models.CharField(max_length=50, blank=True, null=True)
    cultural_affairs_officer = models.CharField(max_length=50, blank=True, null=True)
    departmentrepresentative = models.CharField(max_length=50, blank=True, null=True)

    def get_owner(self):
        return self.owner.email

    def __str__(self):
        return f"{self.owner}"
    
    class Meta:
        verbose_name = "RECORDS"  
        verbose_name_plural = "RECORDS"