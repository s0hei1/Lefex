from pydantic import BaseModel,Field

class DeleteResponse(BaseModel):
    id : int
    message : str = "Delete was successful"
