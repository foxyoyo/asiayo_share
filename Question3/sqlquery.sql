create Table score (
	name VARCHAR(50),
	score float
);
INSERT INTO score (name,score)
values
	('John',97),
	('Mary',100),
	('David',83),
	('Sara',89);

create Table class (
	name VARCHAR(50),
	class VARCHAR(10)
);
INSERT INTO class (name,class)
values
	('John','A'),
	('Mary','A'),
	('David','C'),
	('Sara','B');

WITH ranked_scores AS (
  SELECT s.name, s.score, c.class
  FROM score s
  JOIN class c ON s.name = c.name
  ORDER BY s.score DESC
)
SELECT class
FROM ranked_scores
LIMIT 1 OFFSET 1;
