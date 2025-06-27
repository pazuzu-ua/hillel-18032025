from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from argon2 import PasswordHasher

from models import UserCreate, UserLogin, UserInfo, Token

import jwt
import db

TOKEN_LIFETIME_MINUTES = 60
TOKEN_SECRET_KEY = "cxbghjr6y45tfgfhgh"
TOKEN_ALGORITHM  = "HS256"

ph = PasswordHasher()
security = HTTPBearer()
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post(
        "/register",
        response_model=UserInfo
)
def register_user( user: UserCreate ):
    if db.get_user_by_username( user.username ):
        raise HTTPException( 400, f"Username '{user.username}' is already in use" )
    hashed_password = ph.hash( user.password )
    print( f"Password '{user.password}' hashed to '{hashed_password}' " )
    i_user = db.add_new_user( user.username, hashed_password )
    if not i_user:
        raise HTTPException( 400, "Cannot create a new user" )
    return UserInfo( i_user=i_user, username=user.username )


@router.post(
        "/login",
        response_model=Token
)
def login( user: UserLogin ):
    user_data = db.get_user_by_username(user.username)
    if not user_data:
        raise HTTPException( 400, "Wrong username" )
    try:
        ph.verify( user_data['hashed_password'], user.password )
    except:
        print( user_data['hashed_password'], user.password )
        raise HTTPException( 400, "Wrong password or hash" )
    return Token( access_token=_create_token( user.username ) )

# async необхідний для Depends
async def get_current_user( credentials: HTTPAuthorizationCredentials = Depends(security) ):
    token = credentials.credentials
    try:
        payload = jwt.decode( token, TOKEN_SECRET_KEY, TOKEN_ALGORITHM )
        username = payload.get("sub")
    except:
        raise HTTPException( 400, "Wrong token" )
    user = db.get_user_by_username( username )
    if not user:
        raise HTTPException( 400, "Wrong user" )
    return user


def _create_token( username: str ) -> str:
    exp = datetime.utcnow() + timedelta( minutes=TOKEN_LIFETIME_MINUTES )
    return jwt.encode({
        "sub": username,
        "exp": exp,
    }, TOKEN_SECRET_KEY, TOKEN_ALGORITHM)
