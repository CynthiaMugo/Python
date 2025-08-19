DROP TABLE IF EXISTS club;
CREATE TABLE IF NOT EXISTS club(
    id BIGSERIAL PRIMARY KEY,
    student_id SERIAL REFERENCES student(id),
    name TEXT,
    description TEXT
);
-- above we have one to many relationship
-- between student and club, where one student can join multiple clubs
-- and each club can have multiple students
-- if we want to enforce a one to one relationship, we can use a unique constraint on student_id



-- one to one - use unique constraint to ensure one student can only join one club
-- one to many - use foreign key to allow multiple students to join the same club

-- many to many - use a junction table to allow multiple students to join multiple clubs
-- in this case were using student and subjects

CREATE TABLE IF NOT EXISTS subjects(
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

INSERT INTO subjects (name, description)
VALUES
('Mathematics', 'Study of numbers, quantities, and shapes'),
('Physics', 'Study of matter, energy, and the fundamental forces of nature'),
('Chemistry', 'Study of substances, their properties, and reactions'),
('Biology', 'Study of living organisms and their interactions with the environment'),
('History', 'Study of past events, societies, and cultures'),
('Geography', 'Study of the Earth, its features, and the distribution of life'),
('Computer Science', 'Study of computation, algorithms, and information processing'),
('English Literature', 'Study of written works in the English language')


-- junction table to allow many to many relationship between students and subjects
-- each student can take multiple subjects and each subject can have multiple students

CREATE TABLE IF NOT EXISTS student_subjects(
    student_id SERIAL NOT NULL REFERENCES student(id),
    subject_id BIGSERIAL NOT NULL REFERENCES subjects(id),
    UNIQUE(student_id, subject_id)
);

-- practise on 
-- ON DELETE CASCADE - this will delete all records in the junction table if the student or subject is deleted
-- ON DELETE SET NULL - this will set the student_id or subject_id to NULL in the junction table if the student or subject is deleted
-- ON DELETE RESTRICT - this will prevent deletion of the student or subject if there are records in the junction table