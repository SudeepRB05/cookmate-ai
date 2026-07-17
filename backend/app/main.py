from app.api.recipes import router as recipe_router
from app.api.auth import router as auth_router
from fastapi import FastAPI
from app.database.init_db import init_db

app = FastAPI(
    title="CookMate AI",
    description="AI-powered recipe and cooking assistant app",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(recipe_router)

@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def home():
    return {
        "message": "Welcome to CookMate AI",
        "status": "Backend is running successfully"
    }