from typing import TypedDict


class PlayerData(TypedDict):
    tag: str
    character: str
    alt: str
    offset: tuple[int, int]
    zoom: int


class TournamentData(TypedDict):
    players: list[PlayerData]
    tournament: str
    round: str
