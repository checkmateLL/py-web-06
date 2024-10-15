SELECT DISTINCT sub.subject_name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
JOIN students s ON g.student_id = s.id
WHERE s.student_name = 'Ashley Mcconnell'