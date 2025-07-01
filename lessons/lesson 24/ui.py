# pip install jinja2
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import db

router = APIRouter(prefix="/ui")
templates = Jinja2Templates(directory="templates")

@router.get("/example", response_class=HTMLResponse)
def example_page( request: Request ):
    return templates.TemplateResponse(
        name="example.html",
        request=request,
        context={ "page_title": "Моя динамічна сторінка" },
    )

@router.get("/pets", response_class=HTMLResponse)
def get_pets( request: Request ):
    pets = db.fetch_all_pets()
    return templates.TemplateResponse(
        name="pets.html",
        request=request,
        context={ "pets": pets },
    )
