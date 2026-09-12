from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Home Page</h1>")


def about_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>About Page</h1>")


def contact_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Contact Page</h1>")


def page_number(request: HttpRequest, number: int) -> HttpResponse:
    return HttpResponse(f"<h1>Page: {number}</h1>")


def page_name(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"<h1>Hello {name.title()}!</h1>")
