from django.db import models

class SteamLibrary(models.Model): #done
    game_id = models.ForeignKey(GameID, on_delete = models.CASCADE)
    steam_id = models.ForeignKey(User, on_delete = models.CASCADE)

class GameData(models.Model): #done
    game_id = models.ForeignKey(GameID, on_delete = models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete = models.CASCADE)
    co_op = models.BooleanField(default = False)
    num_players = models.IntegerField(default = None)

class Categories(models.Model): #done
    categories = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30)

class GameID(models.Model): #done
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 15)

class Tally(models.Model):
    game_id = models.ForeignKey(GameID, on_delete = models.CASCADE)
    tally = models.AutoField(primary_key = True)

class User(models.Model): #done
    steam_id = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100)
