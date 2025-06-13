import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import database
import repository
import schemas
from database import get_db
from repository import get_by_id

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.post("/products", response_model=schemas.ProductRead)
def create_product_endpoint(product: schemas.ProductCreate, db: Session = Depends(get_db)) -> schemas.ProductRead:
    return repository.create_product(db, product)


@app.get("/products", response_model=list[schemas.ProductRead])
def get_products(db: Session = Depends(get_db)) -> list[schemas.ProductRead]:
    return repository.get_all(db)


@app.get("/products/{product_id}", response_model=schemas.ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)) -> schemas.ProductRead:
    product = get_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
