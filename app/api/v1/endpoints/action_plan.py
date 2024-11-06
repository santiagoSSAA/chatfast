from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.action_plan_service import MockLLM

router = APIRouter()
llm = MockLLM()

class ActionPlanRequest(BaseModel):
    input_data: str

@router.post("/generate")
async def generate_action_plan(request: ActionPlanRequest):
    try:
        result = llm.generate_action_plan(request.input_data)
        return {"action_plan": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))