import requests


def get_employer(employer):
    """Возвращает информацию о работодателе."""

    url = "https://api.hh.ru/employers"
    params = {
        "text": employer,  # Название компании
        "area": 1,  # Идентификатор региона
        "per_page": 1  # Количество элементов на страницу
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        employer_info = response.json().get("items")
        return employer_info
    else:
        print(f"Не удалось выполнить запрос к API HeadHunter")


def get_vacancies(url_vacancies):
    """Возвращает список вакансий конкретного работодателя по его id."""

    params = {
        "per_page": 100,  # Количество вакансий на вывод (максимум 100)
        "area": 1,  # Идентификатор региона
        "only_with_salary": 'true'  # Только с информацией по зарплате
    }
    response = requests.get(url_vacancies, params=params)
    if response.status_code == 200:
        vacancies = response.json().get("items")
        return vacancies
    else:
        print(f"Не удалось выполнить запрос к API HeadHunter")


result = get_employer('Интеллектуальные робот системы')
url_vacancies = result[0]['vacancies_url']
vacs = get_vacancies(url_vacancies)

for vacancy in vacs:
    company_name = vacancy.get("employer").get("name")
    title = vacancy.get("name")
    vacancy_url = vacancy.get("alternate_url")
    salary = vacancy.get("salary").get("from")
    if salary is None:
        salary = 0
