from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate, RecipeResponse

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)


@router.post("/", response_model=RecipeResponse)
def create_recipe(recipe_data: RecipeCreate, db: Session = Depends(get_db)):
    new_recipe = Recipe(**recipe_data.model_dump())

    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    return new_recipe


@router.get("/", response_model=list[RecipeResponse])
def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()


@router.get("/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return recipe


@router.put("/{recipe_id}", response_model=RecipeResponse)
def update_recipe(recipe_id: int, recipe_data: RecipeCreate, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    for key, value in recipe_data.model_dump().items():
        setattr(recipe, key, value)

    db.commit()
    db.refresh(recipe)

    return recipe


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    db.delete(recipe)
    db.commit()

    return {"message": "Recipe deleted successfully"}