from django.urls import path
from .views import *



urlpatterns = [
    
    path('count/',view_visitor_count),
    path('write/',view_write_cookie),
    path('read/',view_read_cookie),
]
   