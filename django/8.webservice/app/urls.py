from django.urls import path

from app.views import *

urlpatterns = [
    path('', index),
    path('get_students', getStudents),
]