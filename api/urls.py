
from django.urls import path,include
from accounts.views import *

urlpatterns = [
    path('test',TestAPI.as_view(),name="test",),
]
