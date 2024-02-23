from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def counter(request):
    text_file = open("./templates/counter.html", "r")
    page = text_file.read()
    text_file.close()
    return HttpResponse(page)

def basic(request):
    text_file = open("./templates/basic.html", "r")
    page = text_file.read()
    text_file.close()
    return HttpResponse(page)