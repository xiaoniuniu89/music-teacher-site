from django.urls import path
from .views import (
    dashboard,
    agenda
   
)


urlpatterns = [
    path('', dashboard, name='dashboard')
]


htmx_urlpatterns = [
    path('agenda/', agenda, name='agenda')
    
]


urlpatterns += htmx_urlpatterns