-- Create a new database
CREATE DATABASE my_database;

-- Use the database
USE my_database;

-- Create customers table
CREATE TABLE customers (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    country VARCHAR(50),
    score INT
);

-- Insert 5 rows into customers
INSERT INTO customers (id, first_name, country, score) VALUES
(1, 'Pranav', 'Germany', 350),
(2, 'Paramvir', 'India', 900),
(3, 'Sanjana', 'UK', 750),
(4, 'Aditya', 'Germany', 500),
(5, 'Shivam', 'India', 0);

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    sales INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Insert 4 rows into orders
INSERT INTO orders (order_id, customer_id, order_date, sales) VALUES
(1001, 1, '2021-01-11', 35),
(1002, 2, '2021-04-05', 15),
(1003, 3, '2021-06-18', 20),
(1004, 5, '2021-08-31', 10);
