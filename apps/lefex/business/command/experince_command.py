from sqlalchemy.ext.asyncio import AsyncSession
from apps.lefex.data.models.experience import Experience


class ExperienceCommand:

    def __init__(self, db : AsyncSession):
        self.db = db

    async def create(self, experience : Experience):
        self.db.add(experience)
        await self.db.commit()

    async  def Update(self, experience : Experience):
        self.db.add(experience)
