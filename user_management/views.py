from django.shortcuts import render
import json
from django.http import HttpResponse
from django.template import loader
from user_management.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    ul = User.objects.filter()
    title = ul[0].username
    fn = "index"
    template = loader.get_template("index.html")
    context = {
        "title" : title,
        "fn" : fn
    }
    # return HttpResponse("<h1>Hi index</h1> <p>this is index function </p>")
    return HttpResponse(template.render(context, request))


@csrf_exempt
def testREST(request):
    method = request.method

    if(method == "GET"):
        params = request.GET
        # do something
    else :
        payload = request.POST
        # do something


    # return HttpResponse("method is " + method);
    context = {
        "title": method,
        "fn": request.POST
    }
    template = loader.get_template("index.html")
    # return HttpResponse(template.render(context, request))
    response_data = {
        "name" : "natthapach",
        "age" : 21
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
@csrf_exempt
def addUser(req):
    response_data = {
        "result": "fail",
        "method": req.method
    }
    if(req.method == "POST"):
        data = req.POST
        username = data["username"]
        password = data["password"]
        user1 = User(username=username, password=password)
        user1.save()
        response_data = {
            "result":"ok",
            "method":req.method
        }

    return HttpResponse(json.dumps(response_data), content_type="application/json")