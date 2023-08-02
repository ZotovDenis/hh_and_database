import psycopg2

from config import config


class DBManager:
    def __init__(self):
        self.params = config()
        self.conn = psycopg2.connect(database="hh_and_postgres", **self.params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""

        query = "SELECT company, COUNT(*) as vacancies_count FROM vacancies GROUP BY company;"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """

        query = "SELECT * FROM vacancies;"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""

        query = "SELECT AVG(salary) FROM vacancies;"
        self.cur.execute(query)
        result = int(self.cur.fetchone()[0])
        return result

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""

        avg_salary = self.get_avg_salary()
        query = f"SELECT * FROM vacancies WHERE salary > {avg_salary}"
        self.cur.execute(query)
        results = self.cur.fetchall()
        return results

    def get_vacancies_with_keyword(self, word):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова,
        например “python”.
        """

        query = f"SELECT * FROM vacancies WHERE vacancy_title ILIKE '%{word}%'"
        self.cur.execute(query)
        results = self.cur.fetchall()
        return results

    def close_connection(self):
        """Закрываем соединение"""

        self.cur.close()
        self.conn.close()
