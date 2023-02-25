CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
);

INSERT INTO user (email, password) VALUES ('philip@sinnott.st', 'root');