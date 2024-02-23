from django.http import HttpResponse

def index(request):
    text_file = open("./templates/firstview.html", "r")
    data = text_file.read()
    text_file.close()
    return HttpResponse(data)

