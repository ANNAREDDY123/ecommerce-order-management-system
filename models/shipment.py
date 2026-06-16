from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database import Base


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        unique=True
    )

    tracking_number = Column(
        String,
        unique=True
    )

    shipment_status = Column(String)
