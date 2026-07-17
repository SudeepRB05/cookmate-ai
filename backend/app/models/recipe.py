from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)

    cuisine = Column(String(100), nullable=True)
    difficulty = Column(String(50), nullable=True)

    cook_time = Column(Integer, nullable=True)
    servings = Column(Integer, nullable=True)

    ingredients = Column(Text, nullable=False)
    appliances = Column(Text, nullable=True)
    instructions = Column(Text, nullable=False)

    texture_guide = Column(Text, nullable=True)
    plating_tips = Column(Text, nullable=True)
    side_suggestions = Column(Text, nullable=True)

    image_url = Column(String(255), nullable=True)

    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)