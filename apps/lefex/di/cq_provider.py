from apps.lefex.business.command.experince_command import ExperienceCommand
from sqlalchemy.ext.asyncio import  AsyncSession

class CQProvider():

    @classmethod
    def experience_command(cls,db : AsyncSession):
        return ExperienceCommand(db = db)
