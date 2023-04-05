from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    url: str

class SummaryResponseSchema(BaseModel):
    id: int
    url: str
