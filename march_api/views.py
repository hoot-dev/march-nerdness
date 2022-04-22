from rest_framework import generics, status
from rest_framework.response import Response

from .models import Bracket, Team
from users.models import UserPick
from .serializers import (
    BracketSerializer, TeamSerializer, 
    BracketTeamSerializer, UserPickSerializer
)

class UserPickView(generics.CreateAPIView):
    queryset = UserPick.objects.all()
    serializer_class = UserPickSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TeamListView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class BracketCreateView(generics.CreateAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer

class BracketDetailView(generics.RetrieveAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer

class BracketTeamDetailView(generics.RetrieveAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketTeamSerializer