from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Home page for django project")

