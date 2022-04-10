from rest_framework import generics

from .models import Bracket, Team
from .serializers import BracketSerializer, TeamSerializer

class TeamListView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class BracketDetailView(generics.RetrieveAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer