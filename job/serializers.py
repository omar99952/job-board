## model ---> serializer
from .models import job
from rest_framework import serializers

class Jobserializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields= "__all__"