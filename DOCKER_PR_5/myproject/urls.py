from django.urls import path
from myapp.views import profile

urlpatterns = [
    path('api/', profile),
    path('', profile),
]
