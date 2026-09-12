from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Home Page</h1>")


def about_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>About Page</h1>")


def contact_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Contact Page</h1>")
