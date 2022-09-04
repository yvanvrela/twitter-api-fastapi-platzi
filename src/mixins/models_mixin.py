# Pydantic
from pydantic import BaseModel, Field


class IDMixin(BaseModel):
    """ID Model Mixin.

    This mixin is used to add a unique ID field to a model.

    """

    id: int = Field(
        ..., 
        description='Unique ID of the document.'
    )
