CREATE TABLE IF NOT EXISTS parent(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(250) NOT NULL 
);

CREATE TABLE IF NOT EXISTS parent_address(
    id BIGSERIAL PRIMARY KEY,
    parent_id BIGSERIAL REFERENCES parent(id),
    county_name VARCHAR(250),
    town VARCHAR(250),
    longitude REAL,
    latitude REAL,
    house_number VARCHAR(200)
);

INSERT INTO parent (name, email)
VALUES
('Jane Doe', 'jane@gmail.com'),
('John Smith', 'johns@gmail.com');

INSERT INTO parent_address
(county_name, town, longitude, latitude, house_number)
VALUES
('Nairobi', 'Westlands', 36.8219, -1.2921, '123A'),
('Mombasa', 'Nyali', 39.6572, -4.0435, '456B');