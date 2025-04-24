CREATE DATABASE IF NOT EXISTS phonebook_db;

USE phonebook_db;

CREATE TABLE IF NOT EXISTS phonebook (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(15)
);
