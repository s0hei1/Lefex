from pydantic import BaseModel, Field
from typing_extensions import Annotated

DecisionField = Field(min_length=1, max_length=1024, nullable=False)
ExperienceField = Field(min_length=1, max_length=1024, nullable=False)

class ExperienceCreate(BaseModel):
    decision : Annotated[str, DecisionField]
    experience : Annotated[str, ExperienceField]


class ExperienceRead(BaseModel):
    decision : str
    experience : str

class ExperienceUpdate(BaseModel):
    id : int = Annotated[str, Field(min_length=1, max_length=1024, nullable=False)]
    decision : Annotated[str, Field(min_length=1, max_length=1024, nullable=False)]
    experience : Annotated[str, Field(min_length=1, max_length=1024, nullable=False)]
