SELECT s.student_name, AVG(g.grade) as avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.subject_name = 'rest'
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1