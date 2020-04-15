from rest_framework import serializers

from .models import Person, Team, Assignment


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    call_order = serializers.ReadOnlyField(source='assignment.call_order', required=False)
    team_role = serializers.ReadOnlyField(source='assignment.team_role', required=False)

    class Meta:
        model = Person
        depth = 1
        fields = ('id', 'name', 'call_order', 'team_role', 'url',)

class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team')
    person_id = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(), source='person')

    class Meta:
        model = Assignment
        depth = 1
        fields = ('person', 'person_id', 'team_id', 'team_role', 'call_order', 'id', 'url',)
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    members = AssignmentSerializer(source='assignment_set', many=True, read_only=True)

    class Meta:
        model = Team
        depth = 1
        fields = ('id', 'name', 'members', 'url',)