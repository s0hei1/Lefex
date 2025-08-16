from sqlalchemy.ext.asyncio import AsyncSession

class ExperienceRepository:

    def __init__(self, session : AsyncSession):
        self.session = session

    async def create(self, experience : AsyncSession):
        self.session.add(experience)
        await self.session.commit()
