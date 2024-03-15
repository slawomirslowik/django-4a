from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

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