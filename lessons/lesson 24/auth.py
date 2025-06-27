from fastapi import APIRouter

from models import UserCreate, UserLogin, UserInfo, Token


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post(
        "/register",
        response_model=UserInfo
)
def register_user( user: UserCreate ):
    ...


@router.post(
        "/login",
        response_model=Token
)
def login( user: UserLogin ):
    ...
