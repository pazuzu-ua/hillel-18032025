# pip install fastapi uvicorn
from fastapi import FastAPI

# uvicorn app:app                      --- назва_файлу:назва_змінної
# uvicorn app:app --reload
app = FastAPI(
    debug=True,
    title="My Super API",
    description="Description of my API",
    summary="Summary of my API",
    version="8.8.8"
)

@app.get("/")
def index():
    return {
        "bool": True,
        "none": None,
        "str": "hello",
        "num": 44,
        "float": 55.4,
        "arr": [ True, False, None ],
        "tpl": ( 1, 2, 3 ),
        "extra_info": { "success": True }
    }

@app.get("/hello/{name}")
def hello( name: str ):
    return { "msg": f"Hello, {name}!" }

@app.get("/number/{num}")
def number( num: int ):
    return { "msg": f"Your number is {num}." }
