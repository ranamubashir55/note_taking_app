from pydantic import BaseModel


class NotePayloadSchema(BaseModel):
    note_text: str

class NoteResponseSchema(NotePayloadSchema):
    id: int
    note_summary: str