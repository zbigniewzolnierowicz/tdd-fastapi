from fastapi import APIRouter
from app.models.pydantic import SummaryResponseSchema, SummaryPayloadSchema
from app.api import crud

router = APIRouter()

@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def new_summary(payload: SummaryPayloadSchema):
    summary_id = await crud.post(payload)
    response = SummaryResponseSchema(id=summary_id)

    return response
