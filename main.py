from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from models.user import User
from models.customer import Customer
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from models.shipment import Shipment

from routes.auth import router as auth_router
from routes.customers import router as customer_router
from routes.products import router as product_router
from routes.orders import router as order_router
from routes.shipments import router as shipment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce Order Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(customer_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(shipment_router)


@app.get("/")
def home():

    return {
        "message":
        "E-Commerce Order Management System"
    }
