from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Notes(models.Model):
    note_text = fields.TextField()
    note_summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)


NoteSchema = pydantic_model_creator(Notes)