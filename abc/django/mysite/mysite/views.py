#coding=utf-8
from django.http import HttpResponse,Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
def hello(req):
    return HttpResponse("Hello world.")
def hello_man(req,name):
    # raise Http404()
    # assert False
    return HttpResponse("hello %s" % name)
def my_error(req):
    return HttpResponse("Error")
def current_date(req):
    import datetime
    current_date=datetime.datetime.now()
    return render_to_response('current_date.html',locals())
    # now=datetime.datetime.now()
    # return render_to_response('current_date.html',{'current_date':now})
    # t=get_template('current_date.html')
    # html=t.render(Context({'current_date':now}))
    # return HttpResponse(html)
