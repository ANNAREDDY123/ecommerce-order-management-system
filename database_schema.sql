CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50));

CREATE TABLE customers(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE);

CREATE TABLE products(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    price FLOAT,
    stock INTEGER,
    is_active BOOLEAN);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATETIME,
    status VARCHAR(50),
    total_amount FLOAT);

CREATE TABLE order_items(
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price FLOAT);

CREATE TABLE shipments(
    id INTEGER PRIMARY KEY,
    order_id INTEGER UNIQUE,
    tracking_number VARCHAR(100) UNIQUE,
    shipment_status VARCHAR(50)
);
