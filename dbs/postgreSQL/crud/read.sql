-- SELECT <columns>
-- FROM <table>
-- WHERE <READ CONSTRAINT>
-- ORDER BY <LIMIT>

-- read all coulmns

-- SELECT * FROM student;

-- read only email and name

-- SELECT name, email FROM student;

-- filter options with WHERE clause
-- SELECT * FROM student
-- WHERE email = 'johndoe@gmail.com'
-- OR
-- email = 'violet@gmail.com'

SELECT * FROM student
WHERE pocket_money >= 500
AND
pocket_money <= 1700
ORDER BY pocket_money DESC
LIMIT 2