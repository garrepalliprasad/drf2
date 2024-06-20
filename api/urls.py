from django.urls import path
from . import views
urlpatterns=[
    path('student/',views.StudentApi.as_view(),name='student'),
    path('student/<int:pk>/',views.StudentApiDetails.as_view(),name='stud_by_id'),
]