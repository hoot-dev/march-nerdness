from rest_framework import generics

from .models import Bracket
from .serializers import BracketSerializer


class BracketDetail(generics.RetrieveAPIView):
    queryset = Bracket.objects.all()
    serializer_class = BracketSerializer