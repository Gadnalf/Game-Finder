from typing import List, Dict
from fake_useragent import UserAgent
import requests
import urllib.request
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
    print(session.headers)
    print(session.cookies)
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

    custom_ids = re.findall("<a href=\"https://steamcommunity.com/id/(.*?)\">", html)
    ids = re.findall("<a href=\"https://steamcommunity.com/profiles/(.*?)\">", html)
    return custom_ids + ids

#friends = GetFriendsIds("76561198117539193")
#print(GetFriendsIds("peepeepoopoo"))
#print(GetUserInfoFromIds(friends))
print(SearchUsers("gadnalf"))