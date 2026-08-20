SELECT DISTINCT s.student_id, s.student_name
FROM student s
JOIN exam e ON s.student_id = e.student_id
WHERE s.student_id NOT IN (

    -- Students who were highest OR lowest in any exam
    SELECT e1.student_id
    FROM exam e1
    JOIN (
        SELECT exam_id,
               MAX(score) AS mx,
               MIN(score) AS mn
        FROM exam
        GROUP BY exam_id
    ) t
      ON e1.exam_id = t.exam_id
     AND (e1.score = t.mx OR e1.score = t.mn)
)
ORDER BY s.student_id;
