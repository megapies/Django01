from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    title = "index"
    fn = "index"
    template = loader.get_template("index.html")
    context = {
        "title" : title,
        "fn" : fn
    }
    # return HttpResponse("<h1>Hi index</h1> <p>this is index function </p>")
    return HttpResponse(template.render(context, request))
