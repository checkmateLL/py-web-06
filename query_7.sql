SELECT s.student_name, g.grade
FROM students s
JOIN groups gr ON s.group_id = gr.id
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE gr.group_name = 'material' AND sub.subject_name = 'develop'