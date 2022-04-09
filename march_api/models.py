from django.db import models


class Bracket(models.Model):
    name = models.CharField(max_length=100, default='2022 NCAA Bracket')
    slug = models.SlugField(max_length=100, default='2022-ncaa-bracket')

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=20)
    bracket = models.ForeignKey(Bracket, related_name="regions", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Team(models.Model):
    college = models.CharField(max_length=40)
    mascot = models.CharField(max_length=40)
    seed = models.IntegerField(default=0)
    region = models.ForeignKey(Region, related_name="teams", on_delete=models.PROTECT)
    region_position = models.IntegerField() # where located within region
    ppg = models.FloatField()       # points per game
    asm = models.FloatField()       # avg score margin
    rpg = models.FloatField()       # rebounds per game
    oppg = models.FloatField()      # opponent points per game
    orpg = models.FloatField()      # opponent rebounds per game
    fgp = models.FloatField()       # field goal percentage
    ofgp = models.FloatField()      # opponent field goal percentage
    ftp = models.FloatField()       # free throw percentage
    oftp = models.FloatField(default=None)      # opponent free throw percentage
    thpp = models.FloatField()      # three point percentage
    othpp = models.FloatField()     # opponent three point percentage
    twpp = models.FloatField()      # two point percentage
    otwpp = models.FloatField()     # opponent two point percentage
    shooteff = models.FloatField()  # shooting efficiency
    oshooteff = models.FloatField() # opponent shooting efficiency
    fgmpg = models.FloatField()     # field goals made per game
    ofgmpg = models.FloatField()    # opponent field goals made per game
    fgapg = models.FloatField()     # field goals attempted per game
    ofgapg = models.FloatField()    # opponent field goals attempted per game
    thpmpg = models.FloatField()    # three points made per game
    thpapg = models.FloatField()    # three points attempted per game
    ftmpg = models.FloatField()     # free throws made per game
    ftapg = models.FloatField()     # free throws attempted per game
    orpg = models.FloatField()      # offensive rebounds per game
    drpg = models.FloatField()      # defensive rebounds per game
    bpg = models.FloatField()       # blocks per game
    obpg = models.FloatField()      # opponent blocks per game
    spg = models.FloatField()       # steals per game
    ospg = models.FloatField()      # opponent steals per game
    topg = models.FloatField()      # turnovers per game
    otopg = models.FloatField()     # opponent turnovers per game
    pfpg = models.FloatField()      # personal fouls per game
    opfpg = models.FloatField()     # opponent personal fouls per game

    class Meta:
        ordering = ['region_position']
    
    def __str__(self):
        return self.college + ' ' + self.mascot

