from fastapi import APIRouter, HTTPException
from app.models.pydantic import SummaryResponseSchema, SummaryPayloadSchema
from app.models.tortoise import SummarySchema
from app.api import crud
from typing import List

router = APIRouter()

@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def new_summary(payload: SummaryPayloadSchema):
    summary_id = await crud.post(payload)
    response_object = {
        "id": summary_id,
        "url": payload.url
    }

    return response_object

@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary

@router.get("/", response_model=List[SummarySchema])
async def get_all() -> List[SummarySchema]:
    return await crud.get_all()
