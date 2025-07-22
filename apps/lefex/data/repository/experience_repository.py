from sqlmodel import Session


class ExperienceRepository:

    def __init__(self, session : Session):
        self.session = session