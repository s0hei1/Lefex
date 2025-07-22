from sqlmodel import SQLModel, Field


class Experience(SQLModel, table = True):
    id : int = Field(primary_key=True,)
    decision : str = Field(min_length=1, max_length=1024, nullable=False)
    experience : str = Field(min_length=1, max_length=2048, nullable=False)