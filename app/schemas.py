from pydantic import BaseModel


class CharacterResponse(BaseModel):
    id: int
    name: str
    description: str
    actor_id: int

    class Config:
        from_attributes = True


class ActorResponse(BaseModel):
    id: int
    name: str
    nationality: str

    class Config:
        from_attributes = True