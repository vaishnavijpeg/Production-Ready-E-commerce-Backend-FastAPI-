from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.product_service import create_product, get_products

router = APIRouter()

@router.post("/")
def add_product(product, db: Session = Depends(get_db)):
    return create_product(db, product)


@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return get_products(db)
