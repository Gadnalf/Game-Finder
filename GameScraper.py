import requests
import json
from GameData import GameData
from word2number import w2n

def GameDataScraper(steam_iid: str) -> GameData:
    response = requests.get('https://store.steampowered.com/api/appdetails?appids=' + str(steam_iid))

    json = response.json()
    values = json.values()
    data = json[str(steam_iid)]['data'] #get the value from the first key

    short = data.get("short_description").split() #make all the descriptions into lists
    detailed = data.get("detailed_description").split()
    about = data.get("about_the_game").split()
    list = about + short + detailed

    categories = data.get("categories") #get the value of categories key
    tags = [sub['description'] for sub in categories] #get the value of description key\

    name = data.get("name") #to get the name of the game

    num_players=PlayerNumberScraper(list)

    return GameData(name, tags, list, num_players)

def PlayerNumberScraper(list: list) -> GameData:

    player_indicator = ('player','players','friend','friends','player.','players.','friend.','friends.')
    #a list of all potential ways of describing player count that I could find

    indices = [] #to find the indices for all instances of friends or players

    for i in range(len(list)):
        for j in range(len(player_indicator)):
            if list[i].lower() == player_indicator[j]:
                indices.append(i)

    num_players = []

    for i in indices: #to find if any of indices actually means coop
        if list[i - 1].isdigit():
            i = int(i)
            num_players.append(int(list[i - 1]))
        elif not list[i - 1].isdigit():
            try:
                i = w2n.word_to_num(list[i - 1]) #should I return i instead of doing all the logic here?
                num_players.append(i)
            except ValueError:
                pass

    return GameData(num_players)
#print(name)
#print(gameid)
#print(list_categories)
#print(co_op)
#print(list_playercount)

#not sure how to do player tally or getgameinfo


#things we need name, game id, tags, estimated supported play, player tally, getgameinfo
#things we have name, game id, tags, estimated supported play
