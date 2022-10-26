
from http.client import HTTPResponse
from django.http import HttpResponse

def hello_kevin(request):
    return HTTPResponse("Hello Kevin")