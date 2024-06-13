from fastapi import FastAPI

from models import Shelter, Animals


app = FastAPI()

# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
shelters: list[Shelter] = [
    Shelter(
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals=Animals(
            cats=13,
            dogs=15,
        ),
    ),
    Shelter(
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals=Animals(
            cats=12,
            dogs=9,
        ),
    ),
    Shelter(
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals=Animals(
            cats=4,
            dogs=7,
        ),
    ),
]


@app.get("/shelters")
async def get_shelters():
    return shelters


@app.post("/shelters")
async def create_shelter(shelter: Shelter) -> str:
    shelters.append(
        Shelter(name=shelter.name, address=shelter.address, animals=shelter.animals)
    )

    return "Shelter created successfully"


@app.put("/shelters/{shelter_name}")
async def update_shelter(updated_shelter: Shelter, shelter_name: str) -> str:
    for shelter in shelters:
        if shelter.name == shelter_name:
            shelter.address = updated_shelter.address
            shelter.animals = updated_shelter.animals

    return "Shelter updated successfully"


@app.delete("/shelters/{shelter_name}")
async def delete_shelter(shelter_name: str) -> str:
    for shelter in shelters:
        if shelter.name == shelter_name:
            shelters.remove(shelter)
    return "Shelter deleted successfully"
