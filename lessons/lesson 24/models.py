from enum import Enum
from pydantic import BaseModel, Field
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


class AddPet(PetBase):
    ...


class PetInfo(PetBase):
    i_pet: int = Field(
        description="The unique ID of the pet",
        examples=[150],
        gt=0,
    )
