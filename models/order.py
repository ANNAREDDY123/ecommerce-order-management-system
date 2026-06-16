from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from datetime import datetime

from database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )

    order_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    status = Column(String)

    total_amount = Column(
        Float,
        default=0
    )
