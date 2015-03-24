from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.db import connection

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)

    cursor = connection.cursor()
    cursor.execute("SELECT * from users")
    row = cursor.fetchone()
    print row
    return HttpResponse(template.render(context))

def page(request):
	template = loader.get_template('page.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def addUser(request):
	template = loader.get_template('addUser.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))



