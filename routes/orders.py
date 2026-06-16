from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import SessionLocal

from models.order import Order
from models.order_item import OrderItem
from models.product import Product

from schemas.order import OrderCreate

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):

    total_amount = 0

    new_order = Order(
        customer_id=order.customer_id,
        status="Pending"
    )

    db.add(new_order)

    db.commit()

    db.refresh(new_order)

    for item in order.items:

        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if not product.is_active:
            raise HTTPException(
                status_code=400,
                detail="Inactive product cannot be ordered"
            )

        if item.quantity > product.stock:
            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        product.stock -= item.quantity

        item_total = (
            product.price * item.quantity
        )

        total_amount += item_total

        order_item = OrderItem(
            order_id=new_order.id,
            product_id=product.id,
            quantity=item.quantity,
            price=product.price
        )

        db.add(order_item)

    new_order.total_amount = total_amount

    db.commit()

    return {
        "message": "Order created",
        "order_id": new_order.id,
        "total_amount": total_amount
    }


@router.get("/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@router.get("/")
def get_orders(
    status: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Order)

    if status:
        query = query.filter(
            Order.status == status
        )

    total_records = query.count()

    orders = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total_records,
        "current_page": page,
        "data": orders }
