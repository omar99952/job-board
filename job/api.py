# views in rest
from rest_framework import generics
from rest_framework.response import Response
from .models import job
from .serializers import Jobserializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_alljobs(request):
    
    all_jobs = job.objects.all()
    data = Jobserializer(all_jobs,many=True).data
    
    return Response({"data":data})



class JoblistView(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class = Jobserializer
    
    
class Job_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = job.objects.all()
    serializer_class = Jobserializer
    lookup_field = 'id'