from typing import List, Dict
from fake_useragent import UserAgent
import requests
import re

key = "30042FF9A1CAF4AD66072C779330F394"

"""
The following functions raise requests.exceptions.HTTPError if parameters are invalid
"""
def GetFriendsIds(user_id: str) -> List[str]:
    url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={0}&steamid={1}&relationship=friend&format=json".format(key, user_id)

    response = requests.get(url)
    response.raise_for_status()

    friends_list = response.json()['friendslist']['friends']

    friend_ids = []
    for friend in friends_list:
        friend_ids.append(friend['steamid'])

    return friend_ids

def GetOwnedGamesIds(user_id: str) -> List[str]:
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={0}&steamid={1}&format=json".format(key, user_id)

    response = requests.get(url)
    response.raise_for_status()

    game_list = response.json()['response']['games']

    game_ids = []
    for game in game_list:
        game_ids.append(game['appid'])

    return game_ids

def GetUserInfoFromIds(user_ids: List[str]) -> List[Dict[str, str]]:
    comma_separated_user_ids = ",".join(user_ids)
    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}".format(key, comma_separated_user_ids)
    
    response = requests.get(url)
    response.raise_for_status()

    user_info = response.json()["response"]["players"]

    return user_info

def SearchUsers(search_text: str):
    ua = UserAgent()
    session = requests.Session()
    session.get("https://steamcommunity.com/search/users/")
    response = session.get(
        url="https://steamcommunity.com/search/SearchCommunityAjax?text={0}&filter=users&sessionid={1}&steamid_user=false&page=1".format(search_text, str(session.cookies.get('sessionid'))),
        headers={
            "User-Agent": str(ua.chrome),
            "Referer": "https://steamcommunity.com/search/users/",
            "X-Requested-With": "XMLHttpRequest"
        }
    )
    return ParseUserSearch(response.json())

def ParseUserSearch(search_response: Dict[str, str]):
    html = search_response["html"]
    results = re.findall("<div class=\"avatarMedium\"><a href=\"https://steamcommunity.com/(.*?)/(.*?)\"><img src=\"(.*?)\">", html)
    ids = [result[1] if (result[0] == "profiles") else ResolveVanityUrl(result[1]) for result in results]
    pics = [result[2] for result in results]
    persona_name = re.findall("<a class=\"searchPersonaName\" href=\".*?\">(.*?)</a>", html)

    return dict(zip(ids, zip(persona_name, pics)))

def ResolveVanityUrl(vanity_url: str):
    url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={0}&vanityurl={1}".format(key, vanity_url)

    response = requests.get(url)
    response.raise_for_status()
    if response.json()["response"]["success"] == 42:
        return -1

    return response.json()["response"]["steamid"]

#friends = GetFriendsIds("76561198117539193")
#print(GetUserInfoFromIds(friends))
print(SearchUsers("gadnalf"))