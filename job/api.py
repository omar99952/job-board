# views in rest

from rest_framework.response import Response
from .models import job
from .serializers import Jobserializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_alljobs(request):
    
    all_jobs = job.objects.all()
    data = Jobserializer(all_jobs,many=True).data
    
    return Response({"data":data})