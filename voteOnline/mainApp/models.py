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


class MAIN_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
        ('President','President'),
        ('Vice President','Vice President'),
        ('Treasurer','Treasurer'),
        ('Secretary','Secretary'),
        ('Event Coordinator','Event Coordinator'),
        ('Sports and Recreation Officer','Sports and Recreation Officer'),
        ('Cultural affairs officer','Cultural affairs officer'),
        ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"
    
    def __str__(self):
        return f"{self.fullname}"
    
    class Meta:
        verbose_name = "MAIN-WSU Candidate"  
        verbose_name_plural = "MAIN-WSU Candidates"



class CECS_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
         ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)
    

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"


    def __str__(self):
        return f"{self.fullname}"
    
    class Meta:
        verbose_name = "CECS Candidate"  
        verbose_name_plural = "CECS Candidates"


class CSM_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
         ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"
    
    def __str__(self):
        return f"{self.fullname}"
    
    class Meta:
        verbose_name = "CSM Candidate"  
        verbose_name_plural = "CSM Candidates"


class CLA_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
         ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"
    
    def __str__(self):
        return f"{self.fullname}"
    
    class Meta:
        verbose_name = "CLA Candidate"  
        verbose_name_plural = "CLA Candidates"


class CBUS_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
        ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"
    
    def __str__(self):
        return f"{self.fullname}"

    class Meta:
        verbose_name = "CBUS Candidate"  
        verbose_name_plural = "CBUS Candidates"