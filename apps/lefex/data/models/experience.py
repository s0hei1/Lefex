from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class SQLAlchemyBase(DeclarativeBase):
    pass

class Experience(SQLAlchemyBase):
    id : Mapped[int] = mapped_column(primary_key=True)
    decision : Mapped[str] = mapped_column(min_length=1, max_length=1024, nullable=False)
    experience : Mapped[str] = mapped_column(min_length=1, max_length=2048, nullable=False)
