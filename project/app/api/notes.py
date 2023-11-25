import logging
from fastapi import APIRouter, HTTPException
from typing import List
from api import database as db
from models.pydantic import NotePayloadSchema, NoteResponseSchema
from models.tortoise import NoteSchema
from api.text_summarizer import generate_note_summary

log = logging.getLogger("uvicorn")
router = APIRouter()


@router.post("/", response_model=NoteResponseSchema, status_code=201)
async def create_note(payload: NotePayloadSchema, create_summary: bool = False) -> NoteResponseSchema:
    note_summary = ''
    if create_summary:
        try:
            note_summary = generate_note_summary(payload.note_text)
        except Exception as ex:
            log.info(f"Text summariazation Error: {ex}")

    note_id = await db.insert(payload, note_summary)
    response_object = {
        "id": note_id,
        "note_text": payload.note_text,
        "note_summary": note_summary
    }

    return response_object


@router.get("/{id}/", response_model=NoteSchema)
async def read_note(id: int) -> NoteSchema:
    note = await db.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/", response_model=List[NoteSchema])
async def read_all_notes() -> List[NoteSchema]:
    return await db.get_all()


@router.put("/{id}/", status_code=200, response_model=NoteSchema)
async def update_note(id:int, payload: NotePayloadSchema) -> NoteSchema:
    updated_note = await db.update(id, payload)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")

    return updated_note


@router.delete("/{id}/")
async def delete_note(id: int) -> dict:
    note = await db.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    d_count = await db.delete(id)
    if not d_count:
        raise HTTPException(status_code=404, detail=f"Note id {id} not found")
    return {"message": f"Note with id {id} deleted successfully.."}