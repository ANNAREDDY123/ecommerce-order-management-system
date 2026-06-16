from pydantic import BaseModel


class ShipmentCreate(BaseModel):

    order_id: int

    tracking_number: str

    shipment_status: str


class ShipmentUpdate(BaseModel):

    shipment_status: str


class ShipmentResponse(ShipmentCreate):

    id: int

    class Config:
        from_attributes = True
