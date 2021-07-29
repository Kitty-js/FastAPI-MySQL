CREATE DATABASE storedb;
SHOW DATABASES;
USE storedb;
CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR NOT NULL
);