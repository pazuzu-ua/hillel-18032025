from fastapi import APIRouter, HTTPException

from models import PetInfo, AddUpdatePet

import db


# 127.0.0.1:7000 + prefix => 127.0.0.1:7000/pets
router = APIRouter( prefix="/pets", tags=["pets"] )

# 127.0.0.1:7000 + prefix + path
# 127.0.0.1:7000/pets/
@router.get(
        "/", 
        response_model=list[PetInfo],
        summary="List all the pets in the shelter.",
)
def get_pets_list():
    pets = db.fetch_all_pets()
    return pets


@router.get(
    "/{i_pet}", 
    response_model=PetInfo,
    summary="Get information on the pet.",
)
def get_pet_info( i_pet: int ):
    pet = db.fetch_pet_info( i_pet )
    if not pet:
        raise HTTPException( 404, f'Pet with id "{i_pet}" does not exist' )
    return pet


@router.post(
    "/", 
    response_model=PetInfo,
    summary="Create a new pet.",
    status_code=201,
)
def create_pet( pet: AddUpdatePet ):
    pet = db.add_new_pet( pet )
    if not pet:
        raise HTTPException( 500, 'Could not create a pet' )
    return pet


@router.delete(
        "/{i_pet}",
        summary="Delete a pet by ID.",
        status_code=204,
)
def delete_pet( i_pet: int ):
    pet = db.fetch_pet_info( i_pet )
    if not pet:
        raise HTTPException( 404, f'Pet with id "{i_pet}" does not exist' )
    
    result = db.delete_pet( i_pet )
    if not result:
        raise HTTPException( 500, 'Could not delete' )
    
    return None


@router.put(
        "/{i_pet}",
        summary="Update the existing pet.",
        response_model=PetInfo,
)
def update_pet( i_pet: int, pet: AddUpdatePet ):
    pet_info = db.fetch_pet_info( i_pet )
    if not pet_info:
        raise HTTPException( 404, f'Pet with id "{i_pet}" does not exist' )
    
    info = db.update_pet( i_pet, pet )
    if not info:
        raise HTTPException( 500, 'Could not update' )
    
    return info
