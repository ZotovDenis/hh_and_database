from config import config
from database_class import DBManager
from utils import create_database, filling_companies_into_database


def main():
    params = config()
    create_database('hh_and_postgres', params)
    filling_companies_into_database('Ростелеком')
    filling_companies_into_database('Тинькофф')
    filling_companies_into_database('Фабрика Решений')
    filling_companies_into_database('Outlines Technologies')
    filling_companies_into_database('ИнфоТеКС')
    filling_companies_into_database('Профилум')
    filling_companies_into_database('SberTech')
    filling_companies_into_database('ФГБУ СЛО Россия')
    filling_companies_into_database('HR Prime')
    filling_companies_into_database('Аэрофлот')

    db = DBManager()

    # Все компании и количество их вакансий
    companies_and_count = db.get_companies_and_vacancies_count()
    print(f"Все компании и количество их вакансий - {companies_and_count}")

    # Все вакансии
    all_vacancies = db.get_all_vacancies()
    print(f"Все вакансии - {all_vacancies}")

    # Определение средней зарплаты
    avg_salary = db.get_avg_salary()
    print(f"Средняя зарплата - {avg_salary} RUB")

    # Все вакансии с зарплатой выше средней
    salary_higher_avg = db.get_vacancies_with_higher_salary()
    print(f"Все вакансии с зарплатой выше средней - {salary_higher_avg}")

    # Все вакансии, содержащие переданное ключевое слово
    keyword = input("Введите ключевое слово для поиска вакансий, содержащих его: ")
    vacs_with_keyword = db.get_vacancies_with_keyword(keyword)
    print(f"Все вакансии, содержащие слово '{keyword}' - {vacs_with_keyword}")

    # Закрываем соединение
    db.close_connection()


if __name__ == '__main__':
    main()
    input("Press Enter to pay respect :) ")