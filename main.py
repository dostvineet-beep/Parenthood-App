from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="AI Parenting Assistant Suite")

# Mount static files for minimal styling (e.g., Bootstrap/Tailwind from CDN)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Mock data classes
class PlannerInput(BaseModel):
    child_age: int
    school_schedule: str
    family_goals: str
    special_needs: str

class MealsInput(BaseModel):
    family_preferences: str
    dietary_restrictions: str
    budget: float

class EmotionsInput(BaseModel):
    user_type: str  # "parent" or "child"
    mood: str
    notes: str = None

# Home page with links to tools
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )

# --- PLANNER MODULE ---
@app.get("/planner", response_class=HTMLResponse)
async def planner_form(request: Request):
    return templates.TemplateResponse("planner_form.html", {"request": request})

@app.post("/planner", response_class=JSONResponse)
async def planner_submit(
    child_age: int = Form(...),
    school_schedule: str = Form(...),
    family_goals: str = Form(...),
    special_needs: str = Form(None)
):
    # Mock response
    return {
        "planner": {
            "child_age": child_age,
            "school_schedule": school_schedule,
            "family_goals": family_goals,
            "special_needs": special_needs,
            "suggested_routines": [
                "Morning routine at 7:30 AM",
                "Homework time at 5:00 PM",
                "Family dinner at 7:00 PM"
            ],
            "tips": [
                "Encourage regular sleep schedule.",
                "Discuss daily highlights at dinner."
            ]
        }
    }

# --- MEALS MODULE ---
@app.get("/meals", response_class=HTMLResponse)
async def meals_form(request: Request):
    return templates.TemplateResponse("meals_form.html", {"request": request})

@app.post("/meals", response_class=JSONResponse)
async def meals_submit(
    family_preferences: str = Form(...),
    dietary_restrictions: str = Form(...),
    budget: float = Form(...)
):
    # Mock response
    return {
        "meals": {
            "preferences": family_preferences,
            "restrictions": dietary_restrictions,
            "budget": budget,
            "meal_plan": [
                {"name": "Veggie Pasta", "nutrition": "350 kcal"},
                {"name": "Grilled Chicken Salad", "nutrition": "400 kcal"}
            ],
            "grocery_list": ["Pasta", "Chicken breast", "Lettuce", "Tomato", "Olive oil"]
        }
    }

# --- EMOTIONS MODULE ---
@app.get("/emotions", response_class=HTMLResponse)
async def emotions_form(request: Request):
    return templates.TemplateResponse("emotions_form.html", {"request": request})

@app.post("/emotions", response_class=JSONResponse)
async def emotions_submit(
    user_type: str = Form(...),
    mood: str = Form(...),
    notes: str = Form(None)
):
    # Mock response
    return {
        "emotions": {
            "user_type": user_type,
            "mood": mood,
            "notes": notes,
            "suggested_affirmations": [
                "You are strong and loved.",
                "Every day is a new beginning."
            ],
            "coping_strategies": [
                "Take deep breaths.",
                "Share your feelings with someone you trust."
            ]
        }
    }

# --- STRUCTURE FOR DB INTEGRATION ---
# Placeholder comments to indicate where DB logic will go (SQLite/Postgres)
# e.g., import SQLAlchemy, define models, CRUD operations, etc.

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)