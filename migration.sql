CREATE DATABASE crm_sales;

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    date TIMESTAMP NOT NULL,
    price NUMERIC NOT NULL,
    quantity INTEGER NOT NULL,
    product VARCHAR(50) NOT NULL
);