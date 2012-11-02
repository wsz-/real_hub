# Create your views here.
from books.models import *
from django.shortcuts import render_to_response
def books(req):
       all=Book.objects.all()
       return render_to_response('books/books.html',locals())
