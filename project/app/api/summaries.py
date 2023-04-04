from fastapi import APIRouter
from app.models.pydantic import SummaryResponseSchema

router = APIRouter()

@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def new_summary():
    pass
