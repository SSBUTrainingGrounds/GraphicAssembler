from typing import TypedDict


class Character(TypedDict):
    name: str
    alt: str
    offset: tuple[int, int]
    zoom: int


class ThumbnailPlayer(TypedDict):
    tag: str
    character: Character


class ThumbnailData(TypedDict):
    players: list[ThumbnailPlayer]
    tournament: str
    round: str


class Top8Player(TypedDict):
    tag: str
    twitter: str
    placement: int
    main: Character
    secondary: Character
    pocket: Character


class Top8Data(TypedDict):
    players: list[Top8Player]
    tournament: str
    season: int
    number: int
    date: str
    entrants: int
