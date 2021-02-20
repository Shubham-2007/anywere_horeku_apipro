
# from django.contrib import admin
# from django.urls import path
# from file_app import views

# urlpatterns = [
#     path('digit/',views.getimagefromrequest)
# ]

from django.conf.urls import url
from .views import getimagefromrequest

urlpatterns = [
    url(r'^digit/', getimagefromrequest.as_view(), ),
]