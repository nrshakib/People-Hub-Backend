from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from user.serializers import PersonSerializer
from .models import Person

# Create your views here.
def allUsers(request):
    users = Person.objects.all()
    serializer = PersonSerializer(users, many = True)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')

def singleUser(request):
    singleUser = Person.objects.get(id = 1)
    serializer = PersonSerializer(singleUser)
    json_data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type = 'application/json')

