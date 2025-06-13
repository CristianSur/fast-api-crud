from sqlalchemy import select
from sqlalchemy.orm import Session

import schemas
from models import Product


def get_by_id(db: Session, product_id: int):
    stmt = select(Product).where(Product.id == product_id)
    return db.execute(stmt).scalar_one_or_none()

def get_all(db: Session):
    stmt = select(Product)
    return db.execute(stmt).scalars().all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return schemas.ProductRead.model_validate(db_product)