from typing import List

class GameData:
    """Class for holding information about a Steam game

    Attributes:
        id              The game's Steam id
        name            The game's name
        tags            The game's steam tags, i.e. Online Co-op
        num_players     The game's estimated number of players
    """
    id: int
    name: str
    tags: List[str]
    num_players: List[int]

    def __init__(self, id: int, name: str, tags: List[str], num_players: List[int]):
        self.id = id
        self.name = name
        self.tags = tags
        self.num_players = num_players

    def __eq__(self, other):
        return self.id == other.id
