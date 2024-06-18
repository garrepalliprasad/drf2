from django.urls import path
from . import views
urlpatterns=[
    path('student/',views.StudentApi,name='student'),
    path('student/<int:id>/',views.StudentApi,name='stud_by_id'),
]