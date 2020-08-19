from typing import List

class User:
    """Class for storing information about a steam user

    Attributes:
        steam_id        The user's steam id
        name            The user's username
        games           List of steam game ids owned by user
    """
    steam_id: int
    name: str
    games: List[int]

    def __init__(self, steam_id: int, name: str, games: List[int]):
        self.steam_id = steam_id
        self.name = name
        self.games = games

class MainUser(User):
    """Class representing the primary user

    Attributes:
        steam_id        The user's steam id
        name            The user's username
        games           List of steam game ids owned by user
        friends         List of steam profile ids that are friends with the user
    """
    friends: List[int]

    def __init__(self, steam_id: int, name: str, games: List[int], friends: List[int]):
        super(steam_id, name, games)
        self.friends = friends