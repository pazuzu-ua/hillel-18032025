from fastapi import APIRouter, HTTPException
from models import SongInfo, AddUpdateSong
import db

router = APIRouter(prefix="/songs", tags=["songs"])

@router.get(
    "/",
    response_model=list[SongInfo],
    summary="List all the songs in the library"
)
def get_songs_list():
    return db.fetch_all_songs()

@router.get(
    "/{i_song}",
    response_model=SongInfo,
    summary="Get information of song"
)
def get_song_info(i_song: int):
    song = db.fetch_song_info(i_song)
    if not song:
        raise HTTPException(404, f'Song with id "{i_song}" does not exist')
    return song

@router.post(
    "/",
    response_model=SongInfo,
    summary="Create a new song",
    status_code=201,
)
def create_song(song: AddUpdateSong):
    created_song = db.add_new_song(song)
    if not created_song:
        raise HTTPException(500, "Could not create a song")
    return created_song

@router.delete(
    "/{i_song}",
    summary="Delete a song by ID.",
    status_code=204,
)
def delete_song(i_song: int):
    song = db.fetch_song_info(i_song)
    if not song:
        raise HTTPException(404, f'Song with id "{i_song}" does not exist')

    success = db.delete_song(i_song)
    if not success:
        raise HTTPException(500, "Could not delete the song")
    return None

@router.put(
    "/{i_song}",
    summary="Update the existing song by ID.",
    status_code=200,
    response_model=SongInfo,
)
def update_song(i_song: int, song: AddUpdateSong):
    existing = db.fetch_song_info(i_song)
    if not existing:
        raise HTTPException(404, f'Song with id "{i_song}" does not exist')

    updated_song = db.update_song(i_song, song)
    if not updated_song:
        raise HTTPException(500, "Could not update the song")

    return updated_song
