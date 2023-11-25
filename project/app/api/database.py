from models.pydantic import NotePayloadSchema
from models.tortoise import Notes
from typing import Union, List


async def insert(payload: NotePayloadSchema, note_summary:str = '') -> int:
    note = Notes(
        note_text=payload.note_text,
        note_summary=note_summary
    )
    await note.save()
    return note.id


async def get(id: int) -> Union[dict, None]:
    note = await Notes.filter(id=id).first().values()
    if note:
        return note
    return None


async def get_all() -> List:
    all_notes = await Notes.all().values()
    return all_notes


async def update(id: int, payload: NotePayloadSchema) -> int:
    note = await Notes.filter(id=id).update(note_text= payload.note_text)
    if note:
        updated_note = await Notes.filter(id=id).first().values()
        return updated_note
    return None


async def delete(id: int) -> int:
    deleted_count = await Notes.filter(id=id).delete()
    if not deleted_count:
        return None
    else:
        return deleted_count