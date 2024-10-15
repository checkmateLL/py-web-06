SELECT s.student_name, sub.subject_name, g.grade, g.grade_date
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE gr.group_name = 'piece' AND sub.subject_name = 'rest'
AND g.grade_date = (SELECT MAX(grade_date) FROM grades WHERE subject_id = sub.id AND student_id = s.id)
ORDER BY s.student_name;
