from .views import  homeindex,contact,not_404_found
from django.urls import path


urlpatterns = [
    path('contact/',contact,name='contact'),
    path('not-found/',not_404_found,name='not_404_found'),
    path('',homeindex,name='homeindex'),
]