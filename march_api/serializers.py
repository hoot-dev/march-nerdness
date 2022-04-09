from rest_framework import serializers
from .models import Bracket, Region, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
        
class RegionSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ['name', 'teams']
        

class BracketSerializer(serializers.ModelSerializer):
    regions = RegionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Bracket
        fields = ['name', 'regions']