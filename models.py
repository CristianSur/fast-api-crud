from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Float, DateTime

from database import Base


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Product(BaseModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
