import requests
import json


gameid = input('Enter - ')
response=requests.get('https://store.steampowered.com/api/appdetails?appids='+gameid)

json=response.json()
values=json.values()
data=json[gameid]['data'] #get the value from the first key

categories=data.get("categories") #get the value of categories key
list_categories = [ sub['description'] for sub in categories] #get the value of description key
co_op=False
for x in range(len(list_categories)): #co-op checking
    if list_categories[x]=='Co-op' or 'Online Co-op' or 'Multi-player':
        co_op=True

name=data.get("name") #to get the name of the game

short=data.get("short_description").split() #make all the descriptions into lists
detailed=data.get("detailed_description").split()
about=data.get("about_the_game").split()
list=about+short+detailed

player_number=('two','three','four','five','six','seven','eight','2','3','4','5','6','7','8','1-2','1-3','1-4')
player_indicator=('player','players','friend','friends','player.','players.','friend.','friends.')
#a list of all potential ways of describing player count that I could find

indices=[] #to find the indices for all instances of friends or players
for i in range(len(list)):
    for j in range(len(player_indicator)):
        if list[i].lower()==player_indicator[j]:
            indices.append(i)

list_playercount=[]
for s in range(len(indices)): #to find whether any one of those mean coop
    for t in range(len(player_number)):
        if list[indices[s]-1]==player_number[t]:
            list_playercount.append(list[indices[s]-1])

#print(name)
#print(gameid)
#print(list_categories)
#print(co_op)
#print(list_playercount)

#not sure how to do player tally or getgameinfo


#things we need name, game id, tags, estimated supported play, player tally, getgameinfo
#things we have name, game id, tags, estimated supported play
