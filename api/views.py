from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from .serializers import StudentSerializer
from .models import Student
class StudentApi(GenericAPIView,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    lookup_field='id'

    def get(self,request,id=None,*args,**kwargs):
        return self.retrieve(request,id,*args,**kwargs)