from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr


class CustomerResponse(CustomerCreate):
    id: int

    class Config:
        from_attributes = True
