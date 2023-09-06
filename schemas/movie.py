from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Peli", min_length=5, max_length=15)
    overview: str
    year: int = Field(default=2022, le=2022, ge=1)
    rating: float = Field(default=2022, le=20222, ge=1)
    category: str 
    