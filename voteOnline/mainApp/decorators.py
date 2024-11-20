from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from mainApp.models import *
import datetime
import sweetify

def verified_or_superuser(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        profile = request.user
        if profile.verified or profile.is_superuser:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('verify'))

  return wrap

def Records_exist(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        profile = request.user
        if UserRecords.objects.filter(owner=profile):
             return function(request, *args, **kwargs)
        else:
            sweetify.error(request, "You don't have a voting Records yet")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  return wrap


def not_superuser(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if not profile.is_superuser:
               return function(request, *args, **kwargs)
          else:
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     return wrap

def department_not_voted_or_superuser(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if not profile.voted_department or profile.is_superuser:
               return function(request, *args, **kwargs)
          else:
               sweetify.error(request, 'You have already voted!')
               return HttpResponseRedirect(reverse('Records'))
     return wrap


def main_not_voted_or_superuser(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if not profile.voted_main or profile.is_superuser:
               return function(request, *args, **kwargs)
          else:
               sweetify.error(request, 'You have already voted!')
               return HttpResponseRedirect(reverse('Records'))
     return wrap


def CECS_voter_or_superuser(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        profile = request.user
        if profile.department == 'CECS' or profile.is_superuser:
          return function(request, *args, **kwargs)
        else:
          return HttpResponseRedirect('/')

  return wrap


def CECS_schedule_or_superuser(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          try:
               schedule = votingschedule.objects.get(department='CECS')
               start = schedule.start
               end = schedule.end
               today = datetime.datetime.now().date()
               if today >= start and today <= end or request.user.is_superuser:
                    return function(request, *args, **kwargs)
               else:
                    sweetify.error(request, 'Kindly wait for the schedule!')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          except:
               sweetify.error(request, 'There is no schedule posted yet!')
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     return wrap


def CSM_voter_or_superuser(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        profile = request.user
        if profile.department == 'CSM' or profile.is_superuser:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap


def CSM_schedule_or_superuser(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          try:
               schedule = votingschedule.objects.get(department='CSM')
               start = schedule.start
               end = schedule.end
               today = datetime.datetime.now().date()
               if today >= start and today <= end or request.user.is_superuser:
                    return function(request, *args, **kwargs)
               else:
                    sweetify.error(request, 'Kindly wait for the schedule!')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          except:
               sweetify.error(request, 'There is no schedule posted yet!')
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     return wrap


def CLA_voter_or_superuser(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        profile = request.user
        if profile.department == 'CLA' or profile.is_superuser:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap


def CLA_schedule_or_superuser(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          try:
               schedule = votingschedule.objects.get(department='CLA')
               start = schedule.start
               end = schedule.end
               today = datetime.datetime.now().date()
               if today >= start and today <= end or request.user.is_superuser:
                    return function(request, *args, **kwargs)
               else:
                    sweetify.error(request, 'Kindly wait for the schedule!')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          except:
               sweetify.error(request, 'There is no schedule posted yet!')
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     return wrap


def CBUS_voter_or_superuser(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        profile = request.user
        if profile.department == 'CBUS' or profile.is_superuser:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap


def CBUS_schedule_or_superuser(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          try:
               schedule = votingschedule.objects.get(department='CBUS')
               start = schedule.start
               end = schedule.end
               today = datetime.datetime.now().date()
               if today >= start and today <= end or request.user.is_superuser:
                    return function(request, *args, **kwargs)
               else:
                    sweetify.error(request, 'Kindly wait for the schedule!')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          except:
               sweetify.error(request, 'There is no schedule posted yet!')
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     return wrap




def main_schedule_or_superuser(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          try:
               schedule = votingschedule.objects.get(department='Main')
               start = schedule.start
               end = schedule.end
               today = datetime.datetime.now().date()
               if today >= start and today <= end or request.user.is_superuser:
                    return function(request, *args, **kwargs)
               else:
                    sweetify.error(request, 'Kindly wait for the schedule!')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          except:
               sweetify.error(request, 'There is no schedule posted yet!')
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     return wrap
