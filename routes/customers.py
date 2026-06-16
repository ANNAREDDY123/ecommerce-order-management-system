from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import SessionLocal

from models.customer import Customer
from models.order import Order

from schemas.customer import CustomerCreate

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Customer).filter(
        Customer.email == customer.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_customer = Customer(
        name=customer.name,
        email=customer.email
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


@router.get("/{customer_id}/orders")
def get_customer_orders(
    customer_id: int,
    db: Session = Depends(get_db)
):

    orders = db.query(Order).filter(
        Order.customer_id == customer_id
    ).all()

    return orders
