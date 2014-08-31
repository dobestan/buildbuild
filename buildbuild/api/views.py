from django.shortcuts import get_object_or_404
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer

from teams.models import Team
from teams.serializers import TeamSerializer

from projects.models import Project
from projects.serializers import ProjectSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TeamDetail(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = "name"


class TeamUserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        teamname = self.kwargs['name']
        team = get_object_or_404(Team, name=teamname)
        return team.users.all()


class TeamProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        teamname = self.kwargs['name']
        team = get_object_or_404(Team, name=teamname)
        return team.project_set.all()
