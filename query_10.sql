SELECT DISTINCT sub.subject_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
JOIN grades g ON sub.id = g.subject_id
JOIN students s ON g.student_id = s.id
WHERE t.teacher_name = 'Brandon Ray' AND s.student_name = 'Jennifer Watts'