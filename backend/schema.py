from pydantic import BaseModel


class GuestSchema(BaseModel):
    name: str
    present: bool
    marry: bool
    twoday: bool
    food: str
