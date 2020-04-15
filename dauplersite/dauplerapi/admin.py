from django.contrib import admin
from .models import Person, Team, Assignment


class PersonAdmin(admin.ModelAdmin):
    pass


class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    inlines = (AssignmentInline,)


admin.site.register(Person, PersonAdmin)
admin.site.register(Team, TeamAdmin)
