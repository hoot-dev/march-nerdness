from django.contrib import admin

from .models import Team, Region, Bracket, Stat, Matchup


admin.site.register(Team)
admin.site.register(Region)
admin.site.register(Bracket)
admin.site.register(Stat)
admin.site.register(Matchup)
