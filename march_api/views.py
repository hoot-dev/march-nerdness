from rest_framework import generics
from rest_framework import permissions   
from .models import Team
from .serializers import TeamSerializer


class TeamList(generics.ListCreateAPIView):
    """
    List all teams or create a team
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View, edit, or delete a team
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    