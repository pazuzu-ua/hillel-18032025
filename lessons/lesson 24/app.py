from fastapi import FastAPI

from api import router as pet_router
from auth import router as auth_router

import db


app = FastAPI(
    debug=True,
    title="Pet Shelter API",
    description="Manage your pets in your shelter.",
    version="1.1.0",
    openapi_tags=[ 
        { "name": "auth", "description": "Authentification methods" },
        { "name": "pets", "description": "Operations on pets" },
    ],
    on_startup=[ db.init_db ]
)

app.include_router(auth_router)
app.include_router(pet_router)
