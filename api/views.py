from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import team_serializer
from rest_framework.response import Response
from .models import *



class team_viewset(viewsets.ModelViewSet):
    queryset=Team.objects.all()
    serializer_class=team_serializer
    


