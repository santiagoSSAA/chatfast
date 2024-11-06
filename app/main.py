from fastapi import FastAPI
from app.api.v1.endpoints import action_plan

app = FastAPI()

# Incluye las rutas de los endpoints
app.include_router(action_plan.router, prefix="/api/v1/action-plans", tags=["action_plans"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Action Plan API"}