from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, world. This is the main page")

def polls(request):
    return HttpResponse("Hello, world. You're at the polls index.")