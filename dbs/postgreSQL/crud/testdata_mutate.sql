-- SELECT * FROM student
-- WHERE marks >= 80
-- ORDER BY marks DESC

-- ALTER TABLE student 
-- add
-- pocket_money INTEGER;

-- ALTER TABLE student drop
-- COLUMN is_married;

-- UPDATE student
-- SET
-- pocket_money = 2000
-- WHERE marks >= 95;

-- SELECT name, marks, pocket_money FROM student
-- WHERE marks < 50
-- ORDER BY pocket_money DESC
-- LIMIT 15;

UPDATE student
SET marks = '79.5'
WHERE marks = '39.5'