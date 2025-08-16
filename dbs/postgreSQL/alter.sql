-- ALTER STATEMENT
-- ALTER TABLE <table> <instruction<add, drop> <column>>
-- Common Sense

-- initial code before
-- ALTER TABLE student
-- add
-- pocket_money INTEGER;

-- GIVE IT A DEFAULT VALUE OR MAKE IT NULL
-- to make it unique alter in steps
-- create make it null
-- add the data
-- alter statement to constrain the record to not null

-- alter table to ensure pocket money doesnt have null values
-- ALTER TABLE student 
-- ALTER COLUMN pocket_money SET NOT NULL;


-- alter table to drop a column
ALTER TABLE student drop
COLUMN is_married;