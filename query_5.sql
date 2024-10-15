SELECT sub.subject_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.teacher_name = 'Melanie Wilson'