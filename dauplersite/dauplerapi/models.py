from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Assignment')

    def members_list(self):
        return [x.person for x in Assignment.objects.filter(team=self).order_by('call_order')]

    def __str__(self):
        return self.name


class Assignment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_role = models.CharField(max_length=64)
    call_order = models.IntegerField()

    class Meta:
        ordering = ['call_order', ]
