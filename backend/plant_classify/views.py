from .serializers import PlantSerializer
from .models import Plant
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class PlantViewSet(viewsets.ModelViewSet):
    serializer_class=PlantSerializer
    queryset=Plant.objects.all()