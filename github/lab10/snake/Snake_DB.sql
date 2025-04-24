CREATE DATABASE Snake_DB;
USE Snake_DB;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE user_score (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    score INT DEFAULT 0,
    level INT DEFAULT 1,
    snake TEXT,
    direction VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES users(id)
);