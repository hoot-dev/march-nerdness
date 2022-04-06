from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'city', 'mascot', 'ppg', 'asm', 'rpg', 'oppg', 'orpg', 'fgp', 'ofgp', 'ftp', 'oftp', 'thpp', 'othpp', 'twpp', 'otwpp',
            'shooteff', 'oshooteff', 'fgmpg', 'ofgmpg', 'fgapg', 'ofgapg', 'thpmpg', 'thpapg', 'ftmpg', 'ftapg', 'orpg', 'drpg', 'bpg', 'obpg',
            'spg', 'ospg', 'topg', 'otopg', 'pfpg', 'opfpg']