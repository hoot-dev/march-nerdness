from rest_framework import serializers
from .models import Bracket, Matchup, Region, Team, Stat
from users.models import UserPick


class UserPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPick
        fields = '__all__'
        read_only_fields = ['user']

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        exclude = ['id', 'team']


class TeamNoStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ['stats']


class TeamSerializer(serializers.ModelSerializer):
    stats = StatSerializer()

    class Meta:
        model = Team
        exclude = ['region', 'region_position', 'matchup_position']
    
    def create(self, validated_data):
        stats_data = validated_data.pop('stats')
        team = Team.objects.create(**validated_data)
        Stat.objects.create(team=team, **stats_data)
        return team
    
    def to_representation(self, instance):
        """
        determine if we need to return stats or not here
        """
        return super().to_representation(instance)

class MatchupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matchup
        fields = '__all__'
        
        
class RegionSerializer(serializers.ModelSerializer):
    matchups = MatchupSerializer(many=True)

    class Meta:
        model = Region
        fields = ['name', 'matchups']


class RegionTeamSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)

    class Meta:
        model = Region
        fields = ['name', 'teams']
        

class BracketSerializer(serializers.ModelSerializer):
    regions = RegionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Bracket
        fields = ['name', 'regions']
    

class BracketTeamSerializer(serializers.ModelSerializer):
    regions = RegionTeamSerializer(many=True, read_only=True)
    
    class Meta:
        model = Bracket
        fields = ['name', 'regions']
