from django.urls import path

from pages.views import home_page, about_page, contact_page


urlpatterns = [
    path('home/', home_page, name='home'), # type: ignore
    path('about/', about_page, name='about'), # type: ignore
    path('contact/', contact_page, name='contact'), # type: ignore
]
