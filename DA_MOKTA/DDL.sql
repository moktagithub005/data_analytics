-- what is SQL query :A SQL query is a command or instruction written in Structured Query Language (SQL) that you use to talk to a database.

CREATE TABLE persons(
	id INT NOT NULL,
	persons_name VARCHAR(50) NOT NULL,
	birth_date DATE,
	phone VARCHAR(15) NOT NULL,
	CONSTRAINT pk_persons PRIMARY KEY(ID)
)

SELECT *
FROM persons

