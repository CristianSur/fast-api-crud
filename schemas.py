from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int

    model_config = {
        "from_attributes": True
    }