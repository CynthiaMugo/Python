-- update <table_name>
-- SET <columns to update>
-- WHERE - constrain

-- UPDATE student
-- SET
-- marks = 0
-- WHERE marks < 80

-- SELECT name, marks FROM student
-- WHERE marks = 0

UPDATE student
SET email = 'johndoe@doe.com'
WHERE email = 'johndoe@gmail.com'
