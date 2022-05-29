from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import datetime
from django.template import loader  



def index(request):  
   template = loader.get_template('index.htm') # getting our template  
   return HttpResponse(template.render())    


def pre1(request):  
   template = loader.get_template('carsale_before_preprocessing_1.htm') # getting our template  
   return HttpResponse(template.render()) 

def pre2(request):  
   template = loader.get_template('carsale_before_preprocessing_2.htm') # getting our template  
   return HttpResponse(template.render()) 

def post(request):  
   template = loader.get_template('carsale_after_preprocessing.htm') # getting our template  
   return HttpResponse(template.render()) 
def analytics(request):  
   template = loader.get_template('Analytics.htm') # getting our template  
   return HttpResponse(template.render()) 