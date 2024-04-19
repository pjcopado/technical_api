import enum


class RatingWebsiteEnum(str, enum.Enum):
    IMDB = "imdb"
    ROTTEN_TOMATOES = "rotten_tomatoes"
    METACRITIC = "metacritic"
    FILMAFFINITY = "filmaffinity"
    SCREENRANK = "screenrank"
    CINEMASCOPE = "cinemascope"
    REELREVIEWS = "reelreviews"
