from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import SessionLocal

from models.product import Product

from schemas.product import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    new_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        stock=product.stock,
        is_active=product.is_active
    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product


@router.get("/")
def get_products(
    category: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Product)

    if category:
        query = query.filter(
            Product.category == category
        )

    return query.all()
