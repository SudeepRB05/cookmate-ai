from pydantic import BaseModel
from typing import Optional


class RecipeCreate(BaseModel):
    title: str
    description: Optional[str] = None
    cuisine: Optional[str] = None
    difficulty: Optional[str] = None
    cook_time: Optional[int] = None
    servings: Optional[int] = None
    ingredients: str
    appliances: Optional[str] = None
    instructions: str
    texture_guide: Optional[str] = None
    plating_tips: Optional[str] = None
    side_suggestions: Optional[str] = None
    image_url: Optional[str] = None


class RecipeResponse(RecipeCreate):
    id: int
    created_by: Optional[int] = None

    model_config = {
        "from_attributes": True
    }