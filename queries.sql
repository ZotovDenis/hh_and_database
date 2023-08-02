#
SQL-команды для работы с базой данных 'hh_and_postgres' и таблицей 'vacancies'

DROP
DATABASE hh_and_postgres;
CREATE
DATABASE hh_and_postgres;

CREATE TABLE employees
(
    company_id INT,
    company    VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE vacancies
(
    vacancy_id    SERIAL PRIMARY KEY,
    company       VARCHAR(255) REFERENCES employees (company) NOT NULL,
    vacancy_title VARCHAR(255)                                NOT NULL,
    vacancy_url   TEXT,
    salary        INT
);


INSERT INTO employees (company_id, company)
VALUES (%s, %s);

INSERT INTO vacancies (company, vacancy_title, vacancy_url, salary)
VALUES (%s, %s, %s, %s);


SELECT company, COUNT(*) as vacancies_count
FROM vacancies
GROUP BY company;

SELECT *
FROM vacancies;

SELECT AVG(salary)
FROM vacancies;

SELECT *
FROM vacancies
WHERE salary > (SELECT AVG(salary) FROM vacancies);

SELECT *
FROM vacancies
WHERE vacancy_title ILIKE '%sql%';
