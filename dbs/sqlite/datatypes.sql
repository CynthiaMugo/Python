-- first column - id
-- sql syntax variables - lowercase
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL
);

INSERT INTO student (name, email, dob, phone, marks)
VALUES ("Erick", "erick@gmail.com", "2017-07-21", 254722675894, 70.8)

-- SELECT * FROM student
