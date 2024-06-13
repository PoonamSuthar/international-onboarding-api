from sqlalchemy import Column, String, JSON
from app.db.session import Base

class Config(Base):
    __tablename__ = "configs"

    country_code = Column(String, primary_key=True, index=True, unique=True)
    requirements = Column(JSON, nullable=False)

    def __repr__(self):
        return f"<Config(country_code='{self.country_code}', requirements='{self.requirements}')>"
