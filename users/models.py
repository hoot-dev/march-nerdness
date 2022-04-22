from django.db import models
from django.contrib.auth import get_user_model
from march_api.models import Matchup, Team

User = get_user_model()

# Create your models here.
class UserPick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    matchup = models.ForeignKey(Matchup, on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)