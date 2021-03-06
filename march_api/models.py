from django.db import models


class Bracket(models.Model):
    name = models.CharField(max_length=100, default='2022 NCAA Bracket')
    slug = models.SlugField(max_length=100, default='2022-ncaa-bracket')

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=10)
    bracket = models.ForeignKey(Bracket, related_name="regions", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Team(models.Model):
    college = models.CharField(max_length=40, unique=True)
    mascot = models.CharField(max_length=40)
    seed = models.IntegerField(null=True, blank=True)
    region = models.ForeignKey(Region, related_name="teams", null=True, blank=True, 
                               on_delete=models.CASCADE)
    region_position = models.SmallIntegerField(null=True, blank=True)
    position_choices = [
        ('top', 'Top'),
        ('bot', 'Bottom')
    ]
    matchup_position = models.CharField(max_length=3, choices=position_choices, 
                                        null=True, blank=True) # top or bottom of matchup
    
    def __str__(self):
        return self.college + ' ' + self.mascot
    
    class Meta:
        ordering = ['region_position']


class Stat(models.Model):
    team = models.OneToOneField(Team, related_name="stats", on_delete=models.CASCADE, null=True, blank=True)
    ppg = models.FloatField()       # points per game
    opp_ppg = models.FloatField()      # opponent points per game
    avg_score_margin = models.FloatField()       # avg score margin
    reb_pg = models.FloatField()       # rebounds per game
    opp_reb_pg = models.FloatField()      # opponent rebounds per game
    fgp = models.FloatField()       # field goal percentage
    opp_fgp = models.FloatField()      # opponent field goal percentage
    ftp = models.FloatField()       # free throw percentage
    opp_ftp = models.FloatField()      # opponent free throw percentage
    thpp = models.FloatField()      # three point percentage
    opp_thpp = models.FloatField()     # opponent three point percentage
    twpp = models.FloatField()      # two point percentage
    opp_twpp = models.FloatField()     # opponent two point percentage
    shoot_eff = models.FloatField()  # shooting efficiency
    opp_shoot_eff = models.FloatField() # opponent shooting efficiency
    fgmpg = models.FloatField()     # field goals made per game
    opp_fgmpg = models.FloatField()    # opponent field goals made per game
    fgapg = models.FloatField()     # field goals attempted per game
    opp_fgapg = models.FloatField()    # opponent field goals attempted per game
    thpmpg = models.FloatField()    # three points made per game
    thpapg = models.FloatField()    # three points attempted per game
    opp_thpmpg = models.FloatField() # opponent three points made per game
    opp_thpapg = models.FloatField() # opponent three points attempted per game
    ftmpg = models.FloatField()     # free throws made per game
    ftapg = models.FloatField()     # free throws attempted per game
    opp_ftmpg = models.FloatField() # opponent free throws made per game
    opp_ftapg = models.FloatField() # opponent free throws attempted per game
    off_rpg = models.FloatField()      # offensive rebounds per game
    def_rpg = models.FloatField()      # defensive rebounds per game
    opp_off_rpg = models.FloatField() # opponent offensive rebounds per game
    opp_def_rpg = models.FloatField() # opponent defensive rebounds per game
    bpg = models.FloatField()       # blocks per game
    opp_bpg = models.FloatField()      # opponent blocks per game
    spg = models.FloatField()       # steals per game
    opp_spg = models.FloatField()      # opponent steals per game
    topg = models.FloatField()      # turnovers per game
    opp_topg = models.FloatField()     # opponent turnovers per game
    pfpg = models.FloatField()      # personal fouls per game
    opp_pfpg = models.FloatField()     # opponent personal fouls per game

    def __str__(self):
        return self.team.college + ' stats'


class Matchup(models.Model):
    region = models.ForeignKey(Region, related_name="matchups", null=True, blank=True, 
                               on_delete=models.CASCADE)
    bracket = models.ForeignKey(Bracket, related_name="matchups", on_delete=models.CASCADE,
                                null=True, blank=True)
    round = models.IntegerField()
    team_a = models.ForeignKey(  
		Team,
		on_delete=models.SET_NULL,
		related_name="team_a",
		null=True,
		blank=True
	)
    team_b = models.ForeignKey(  
		Team,
		on_delete=models.SET_NULL,
		related_name="team_b",
		null=True,
		blank=True
	)

    team_a_score = models.IntegerField(default=0)
    team_b_score = models.IntegerField(default=0)

    winner = models.ForeignKey(  
		Team,
		on_delete=models.SET_NULL,
		related_name="winner",
		null=True,
		blank=True
	)

    game_date_time = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return "Game #: {}".format(self.id)

    class Meta:
        ordering = ['id']