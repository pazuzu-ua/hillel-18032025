from fastapi import FastAPI

from api import router as song_router

import db

app = FastAPI(
    debug=True,
    title="Song Library System",
    description="Manage your liked Songs",
    version="1.0.0",
    openapi_tags=[{ "name": "songs", "description": "Operations on Songs" }],
    on_startup=[db.init_db]
)

app.include_router(song_router)