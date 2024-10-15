SELECT s.student_name, t.teacher_name, AVG(g.grade) as avg_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE t.teacher_name = 'Dustin Haas' AND s.student_name = 'April Hampton'
GROUP BY s.id, t.id;