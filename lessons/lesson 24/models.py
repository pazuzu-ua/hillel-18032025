from enum import Enum
from pydantic import BaseModel, Field, computed_field
from datetime import date


class PetTypeEnum(str, Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"

class PetBase(BaseModel):
    name: str = Field(
        description="The name of the pet",
        examples=["Fluffy"],
        min_length=1,
    )
    date_of_birth: date = Field(
        description="The date of birth of the pet",
        examples=["2020-02-20"],
    )
    pet_type: PetTypeEnum = Field(
        description="The type of the pet",
        examples=[ PetTypeEnum.CAT ],
    )
    vaccinated: bool = Field(
        description="Indicates whether the pet has been vaccinated",
        examples=[ True ],
    )


class AddUpdatePet(PetBase):
    ...


class PetInfo(PetBase):
    i_pet: int = Field(
        description="The unique ID of the pet",
        examples=[150],
        gt=0,
    )

    @computed_field
    @property
    def age(self) -> int:
        today = date.today()
        delta = today - self.date_of_birth
        return delta.days // 365


class UserCreate(BaseModel):
    username: str = Field(
        description="The unique login of the user",
        examples=["user_login"],
        min_length=3,
    )
    password: str = Field(
        description="The password of the user.",
        examples=["Cvrtg46ergfr"],
        min_length=6,
    )

class UserLogin(BaseModel):
    username: str
    password: str


class UserInfo(BaseModel):
    i_user: int
    username: str


class Token(BaseModel):
    access_token: str
