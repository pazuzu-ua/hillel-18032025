from fastapi import APIRouter, HTTPException

from models import SongInfo,AddSong
import db

router = APIRouter( prefix="/songs", tags=["songs"])

@router.get("/", 
            response_model=list[SongInfo],
            summary="List all the songs in the library")
def get_songs_list():
    songs = db.fetch_all_songs()
    return  songs
    
@router.get(
    "/{i_song}",
    response_model=SongInfo,
    summary="Get information of song"
)

def get_song_info(i_song: int):
    song = db.fetch_song_info( i_song )
    if not song:
        raise HTTPException( 404, f'Song with id "{i_song}" does not exist' )
    return song



@router.post(
     "/", 
    response_model=SongInfo,
    summary="Create a new song",
    status_code=201,
)   

def create_song(song:AddSong):
    song = db.add_new_song(song)
    if not song:
        raise HTTPException( 500, 'Could not create a song' )
    return song

@router.delete(
        "/{i_song}",
        summary="Delete a song by ID.",
        status_code=204,
)
def delete_song( i_song: int ):
    song = db.fetch_song_info( i_song )
    if not song:
        raise HTTPException( 404, f'Pet with id "{i_song}" does not exist' )
    
    result = db.delete_song( i_song )
    if not result:
        raise HTTPException( 500, 'Could not delete' )
    
    return None

def update_song( i_song: int, song: AddSong ):
    ... 