import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
    <!doctype html>
    <title>Hello World</title>
    <h1>Hello World</h1>
    <p>Hello World</p>
    """)

def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse("""
    <h1>Current Datetime: {now} </h1>
    """)