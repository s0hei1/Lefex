from fastapi import APIRouter

from apps.lefex.business.schemas.experience_schema import ExperienceRead, ExperienceCreate

experience_router = APIRouter(tags=["experience"], prefix="/experience")


@experience_router.post("/create", response_model=ExperienceRead)
async def create_experience(experience: ExperienceCreate):

    return {"id" : 1, "experience" : experience.experience, "decision" : experience.decision}
