SELECT t.teacher_name, AVG(g.grade) as avg_grade
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
JOIN grades g ON sub.id = g.subject_id
WHERE t.teacher_name = 'Michele Ellison'
GROUP BY t.id