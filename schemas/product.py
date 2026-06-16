from pydantic import BaseModel, Field


class ProductCreate(BaseModel):

    name: str

    category: str

    price: float = Field(
        gt=0
    )

    stock: int = Field(
        ge=0
    )

    is_active: bool = True


class ProductResponse(ProductCreate):

    id: int

    class Config:
        from_attributes = True
