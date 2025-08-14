CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL,
    is_married BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO student (name,email,dob,phone,marks,is_married)
VALUES ('alice', 'alice@gmail.com', '2002-05-14', 254732323, 88.2, TRUE);