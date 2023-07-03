from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from databases.db_conn import Base


class Item(Base):
    __tablename__ = "items"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, index=True)
    description: str = Column(String, index=True)
    owner_id: int = Column(Integer, ForeignKey("users.id"))

