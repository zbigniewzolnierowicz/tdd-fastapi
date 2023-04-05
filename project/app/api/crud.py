from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

async def post(new_summary: SummaryPayloadSchema):
    summary = TextSummary(
        url=new_summary.url,
        summary="dummy_summary"
    )
    await summary.save()
    return summary.id

