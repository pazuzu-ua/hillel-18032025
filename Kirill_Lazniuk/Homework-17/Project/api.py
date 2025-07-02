from fastapi import APIRouter

from models import SongInfo
import db

router = APIRouter( prefix="/songs", tags=["songs"])

@router.get("/", 
            response_model=list[SongInfo],
            summary="List all the songs in the library")
def get_songs_list():

    songs = db.fetch_all_songs()
    print(songs)


    return [
        SongInfo(
            i_song=12,
            name="I peek you",
            genre="hyperpop",
            release_date="2023-02-12",
            author_name="Fortuna812",
            is_popular=True,
        )
            
    ]
