from rest_framework import serializers

from .models import Person, Team, Assignment


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        depth = 1
        fields = ('person', 'team_role', 'call_order')


class TeamSerializer(serializers.ModelSerializer):
    members = AssignmentSerializer(source='assignment_set', many=True)

    class Meta:
        model = Team
        depth = 1
        fields = ('name', 'members')

class PersonSerializer(serializers.ModelSerializer):
    call_order = serializers.Field(source='assignment.call_order', required=False)
    team_role = serializers.Field(source='assignment.team_role', required=False)

    class Meta:
        model = Person
        depth = 1
        fields = ('name', 'call_order', 'team_role')
