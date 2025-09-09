from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from schemas import *
from models import Product
from schemas import ProductRead


def get_by_id(db: Session, product_id: int) -> Optional[ProductRead]:
    stmt = select(Product).where(Product.id == product_id)
    product = db.execute(stmt).scalar_one_or_none()

    if product is None:
        return None

    return ProductRead.model_validate(product)


def get_all(db: Session) -> list[ProductRead]:
    stmt = select(Product)
    products = db.execute(stmt).scalars().all()
    return [ProductRead.model_validate(p) for p in products]


def create_product(db: Session, product: ProductCreate) -> ProductRead:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return ProductRead.model_validate(db_product)
