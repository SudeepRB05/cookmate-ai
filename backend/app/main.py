from fastapi import FastAPI

app = FastAPI(
    title="CookMate AI",
    description="AI-powered recipe and cooking assistant app",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CookMate AI",
        "status": "Backend is running successfully"
    }