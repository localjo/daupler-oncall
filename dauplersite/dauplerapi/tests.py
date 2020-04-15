from django.test import TestCase, Client
import json
from .models import Person, Team, Assignment

class TeamsListTest(TestCase):
    """ Sorts teams according to call_order """

    def setUp(self):
        Team.objects.create(name='Engineering')
        Person.objects.create(name='Jo')
        Person.objects.create(name='Sam')
        Person.objects.create(name='Bobby')
        Assignment.objects.create(team_id=1, person_id=1, team_role='Cat', call_order=3)
        Assignment.objects.create(team_id=1, person_id=2, team_role='Dog', call_order=2)
        Assignment.objects.create(team_id=1, person_id=3, team_role='Wombat', call_order=1)

    def test_members_list(self):
        my_team = Team.objects.get(id=1)
        person_1 = Person.objects.get(id=1)
        person_2 = Person.objects.get(id=2)
        person_3 = Person.objects.get(id=3)
        all_members = my_team.members_list()
        self.assertEqual(all_members[0], person_3)
        self.assertEqual(all_members[1], person_2)
        self.assertEqual(all_members[2], person_1)

    def test_teams_api_response(self):
        client = Client()
        response = client.get('/teams/')
        json_content = json.loads(response.content)
        expected = ', '.join(member['person']['name'] for member in json_content[0]['members'])
        # json_expected = json.loads()
        self.assertEqual(expected, 'Bobby, Sam, Jo')