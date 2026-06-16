# ecommerce-order-management-system
E-Commerce Order Management System built with FastAPI, SQLAlchemy, SQLite, JWT Authentication, Order Processing, Shipment Tracking, Pagination, Filtering, Background Tasks, and Role-Based Access Control.
# E-Commerce Order Management System

## Overview

A FastAPI-based backend application for managing customers, products, orders, and shipments with JWT Authentication and SQLAlchemy ORM.

## Features

* JWT Authentication
* Customer Management
* Product Management
* Order Management
* Shipment Management
* Pagination
* Filtering & Search
* SQLAlchemy ORM
* SQLite Database
* Swagger Documentation
* CORS Support

## APIs

### Authentication

* POST /auth/register
* POST /auth/login

### Customers

* POST /customers
* GET /customers/{customer_id}/orders

### Products

* POST /products
* GET /products
* GET /products?category=electronics

### Orders

* POST /orders
* GET /orders
* GET /orders/{id}
* GET /orders?status=Pending
* GET /orders?page=1&limit=10

### Shipments

* POST /shipments
* PUT /shipments/{id}
* GET /shipments/{id}
* GET /shipments?status=Shipped

## Business Rules

* Prevent ordering inactive products
* Prevent negative stock
* Auto-calculate order total
* Reduce stock after order creation
* One shipment per order
* Unique tracking number

## Run Project

pip install -r requirements.txt

uvicorn main:app --reload

## Swagger

http://127.0.0.1:8000/docs
