from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import List

async def post(new_summary: SummaryPayloadSchema) -> TextSummary:
    summary = TextSummary(
        url=new_summary.url,
        summary="dummy_summary"
    )
    await summary.save()
    return summary.id

async def get(summary_id: int) -> dict | None:
    summary = await TextSummary.filter(id=summary_id).first().values()
    if summary:
        return summary
    return None

async def get_all() -> List[TextSummary]:
    summaries = await TextSummary.all().values()
    return summaries
