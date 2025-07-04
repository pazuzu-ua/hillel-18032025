from enum import Enum
from pydantic import BaseModel, Field
from datetime import date


class SongsGenreEnum(str, Enum):
    HYPERPOP = "hyperpop"
    DRAIN = "drain"
    HIPHOP = "hiphop"
    ROCK = "rock"


class SongBase(BaseModel):
    name: str = Field(
        description="The name of the song",
        examples=["ParisLove"],
        min_length=1,
    )
    author_name: str = Field(
        description="The author name of the song",
        examples=["Fortuna812"],
        min_length=1,
    )
    genre: SongsGenreEnum = Field(
        description="The genre of the song",
        examples=[ SongsGenreEnum.HYPERPOP ],
        min_length=1,
    )
    release_date: date = Field(
         description="The release date of the song",
         examples=["2024-02-20"]
    )
    is_popular: bool = Field(
        description="True if the track has more than 1,000,000 plays",
        examples=[True]
    )

class AddSong(SongBase):
    ...


class SongInfo(SongBase):
    i_song: int = Field(
        description="The ID of the song",
        examples=[12],
        gt=0,
    )
