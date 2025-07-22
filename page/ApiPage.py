import requests
import pytest  # noqa
from selenium.webdriver.common.by import By
import allure


class ApiPage:
    BASE_URL = "https://ariadne.aviasales.com/api/v1/seo/footer"

    def __init__(self, driver):
        """
        Конструктор класса ApiPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = "https://www.aviasales.ru"
        self.to_input = (By.CSS_SELECTOR, "#avia_form_destination-input")
        self.departure_date_input = (By.CSS_SELECTOR, '[data-test-id="start-date-field"]')  # noqa
        self.return_date_input = (By.CSS_SELECTOR, '[data-test-id="end-date-value"]')  # noqa
        self.search_button = (By.CSS_SELECTOR, '[data-test-id="form-submit"]')

    @staticmethod
    @allure.step("Информация о популярных направлениях")
    def get_popular_destinations():
        """
        Ввод параметров для поиска популярного наравления.
        """
        params = {
            "language": "ru",
            "brand": "AS",
            "market": "ru",
            "currency": "rub",
            "popular_destinations": "true"
        }
        response = requests.get(ApiPage.BASE_URL, params=params)
        return response  # возвращаем весь объект ответа

    @allure.step("Информация о городе вылета")
    def get_nearest_places(locale='ru_RU'):
        """
        Ввод параметров для вывода о городе вылета.
        """
        url = 'https://suggest.aviasales.com/v2/nearest_places.json'
        params = {
            'locale': locale
        }
        response = requests.get(url, params=params)
        return response

    @allure.step("Стоимость билета по несуществующей дате")
    def get_price_matrix(origin_iata, destination_iata, depart_start, depart_range=6):  # noqa
        url = "https://explore-api.aviasales.ru/api/v1/price_matrix.json"
        """
        Ввод параметров для получения информации указанием невалидных данных.
        """
        params = {
            'origin_iata': origin_iata,
            'destination_iata': destination_iata,
            'depart_start': depart_start,
            'depart_range': depart_range,
            'affiliate': 'false',
            'market': 'ru'
        }
        return requests.get(url, params=params)

    @allure.step("Вывод стоимостей билета с некорретным методом")
    def put_ticket_price(origin_iata, destination_iata, depart_start, depart_range=6):  # noqa
        url = "https://explore-api.aviasales.ru/api/v1/price_matrix.json"
        """
        Ввод параметров для получения информации по стоимости билетов.
        """
        params = {
            'origin_iata': origin_iata,
            'destination_iata': destination_iata,
            'depart_start': depart_start,
            'depart_range': depart_range,
            'affiliate': 'false',
            'market': 'ru'
        }
        return requests.put(url, params=params)

    @allure.step("Вывод билета без указания даты вылета")
    def get_price_no_depart_months():
        url = "https://explore-api.aviasales.ru/api/v1/price_matrix.json"
        """
        Ввод параметров для получения информации указанием невалидных данных.
        """
        params = {
            'brand': 'AS',
            'currency': 'RUB',
            'depart_months[]': '',
            'destination': 'MOW',
            'direct': 'false',
            'market': 'ru',
            'one_way': 'true',
            'origin': 'IJK',
            'trip_class': 'Y'
        }
        response = requests.get(url, params=params)
        return response
