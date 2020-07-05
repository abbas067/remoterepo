from django.shortcuts import render
from django.http import HttpResponse
import datetime
def date_time_view(request):
    user=request.user
    print("user name:",user)
    date=datetime.datetime.now()
    s='<h1>The Current Date and Time At Server is'+str(date)+'</h1>'
    return HttpResponse(s)
