-- SELECT * FROM  parent
-- WHERE student_id = 56;

SELECT * FROM parent
LEFT JOIN student ON parent.student_id = student.id;