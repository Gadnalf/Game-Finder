from typing import List

class User:
    """Class for storing information about a steam user

    Attributes:
        id              The user's steam id
        name            The user's username
        games           List of steam game ids owned by user
    """
    id: int
    name: str
    games: List[int]

    def __init__(self, id: int, name: str, games: List[int]):
        self.id = id
        self.name = name
        self.games = games

class MainUser(User):
    """Class representing the primary user

    Attributes:
        id              The user's steam id
        name            The user's username
        games           List of steam game ids owned by user
        friends         List of steam profile ids that are friends with the user
    """
    friends: List[int]

    def __init__(self, id: int, name: str, games: List[int], friends: List[int]):
        super(id, name, games)
        self.friends = friends