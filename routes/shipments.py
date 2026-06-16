from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import SessionLocal

from models.shipment import Shipment
from models.order import Order

from schemas.shipment import (
    ShipmentCreate,
    ShipmentUpdate
)

router = APIRouter(
    prefix="/shipments",
    tags=["Shipments"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_shipment(
    shipment: ShipmentCreate,
    db: Session = Depends(get_db)
):

    order = db.query(Order).filter(
        Order.id == shipment.order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    existing_order = db.query(Shipment).filter(
        Shipment.order_id == shipment.order_id
    ).first()

    if existing_order:
        raise HTTPException(
            status_code=400,
            detail="Shipment already exists"
        )

    existing_tracking = db.query(Shipment).filter(
        Shipment.tracking_number ==
        shipment.tracking_number
    ).first()

    if existing_tracking:
        raise HTTPException(
            status_code=400,
            detail="Tracking number already exists"
        )

    new_shipment = Shipment(
        order_id=shipment.order_id,
        tracking_number=shipment.tracking_number,
        shipment_status=shipment.shipment_status
    )

    db.add(new_shipment)

    db.commit()

    db.refresh(new_shipment)

    return new_shipment


@router.put("/{shipment_id}")
def update_shipment(
    shipment_id: int,
    shipment: ShipmentUpdate,
    db: Session = Depends(get_db)
):

    db_shipment = db.query(Shipment).filter(
        Shipment.id == shipment_id
    ).first()

    if not db_shipment:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"
        )

    db_shipment.shipment_status = (
        shipment.shipment_status
    )

    db.commit()

    return {
        "message":
        "Shipment updated"
    }


@router.get("/{shipment_id}")
def get_shipment(
    shipment_id: int,
    db: Session = Depends(get_db)
):

    shipment = db.query(Shipment).filter(
        Shipment.id == shipment_id
    ).first()

    if not shipment:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"
        )

    return shipment


@router.get("/")
def get_shipments(
    status: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Shipment)

    if status:
        query = query.filter(
            Shipment.shipment_status == status
        )

    return query.all()
