from django.urls import path
from .views import Test

urlpatterns = [
    path('test', Test.as_view({'get': 'method'})),
    path('user', Test.as_view({'get': 'user', 'post': 'user'}))
]
