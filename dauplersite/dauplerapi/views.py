from rest_framework import viewsets

from .serializers import PersonSerializer, TeamSerializer, AssignmentSerializer
from .models import Person, Team, Assignment


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all().order_by('call_order')
    serializer_class = AssignmentSerializer
