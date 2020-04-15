from rest_framework import viewsets

from .serializers import PersonSerializer, TeamSerializer, AssignmentSerializer
from .models import Team

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer

