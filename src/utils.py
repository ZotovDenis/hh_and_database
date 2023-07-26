from typing import Any

import psycopg2

from config import config
from hh_api import get_employer, get_vacancies


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о вакансиях."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                company VARCHAR(255) NOT NULL,
                vacancy_title VARCHAR(255) NOT NULL,
                vacancy_url TEXT,
                salary INTEGER
            )
        """)

    conn.commit()
    conn.close()


def filling_database(data: list[dict[str, Any]], database_name: str, params: dict):
    """Внесение информации по вакансиям в таблицу vacancies."""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for vacancy in data:

            company = vacancy.get("employer").get("name")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            salary = vacancy.get("salary").get("from")
            if salary is None:
                salary = 0

            cur.execute(
                """
                INSERT INTO vacancies (company, vacancy_title, vacancy_url, salary)
                VALUES (%s, %s, %s, %s)
                """,
                (company, vacancy_title, vacancy_url, salary)
            )
    conn.commit()
    conn.close()


def filling_companies_into_database(company_name):
    """Добавление вакансий компании company_name, название которой было передано на вход функции."""

    params = config()
    result = get_employer(company_name)
    url_vacancies = result[0]['vacancies_url']
    vacs = get_vacancies(url_vacancies)
    filling_database(vacs, 'hh_and_postgres', params)
