from page.ApiPage import ApiPage
import pytest  # noqa
import allure


@allure.epic("API Tests")
@allure.description("Получение списка популярных направлений")
@allure.feature("Популярные направления")
def test_popular_destinations():
    with allure.step("Получаем популярные направления"):
        response = ApiPage.get_popular_destinations()

    assert response.status_code == 200
    data = response.json()

    assert "popular_destinations" in data
    assert isinstance(data["popular_destinations"], list)


@allure.epic("API Tests")
@allure.description("Получение информации о городе вылета")
@allure.feature("Информация о городе вылета")
def test_nearest_places():
    with allure.step("Получаем информацию о городе вылета"):
        response = ApiPage.get_nearest_places()
    assert response.status_code == 200
    data = response.json() 

    assert isinstance(data, list)
    assert len(data) > 0

    first_place = data[0]
    assert isinstance(first_place, dict)
    assert 'name' in first_place
    assert 'code' in first_place

    assert 'coordinates' in first_place
    assert 'lat' in first_place['coordinates']
    assert 'lon' in first_place['coordinates']


@allure.epic("API Tests")
@allure.description("Получение информации о билете, негативный тест")
@allure.feature("Вывод стоимости билета при указании несуществующей даты")
def test_price_matrix_with_invalid_date():
    with allure.step("Запрос с некорректной датой вылета"):
        response = ApiPage.get_price_matrix(
            origin_iata='IJK',
            destination_iata='MOW',
            depart_start='2025-02-29',
            depart_range=6
        )
    # Проверка статус кода
    assert response.status_code == 400


@allure.epic("API Tests")
@allure.description("Получение информации о билете с некорректно выбранным методом") # noqa
@allure.feature("Метод PUT стоимость билетов на рейсы Ижевск-Москва 01.08.25")
def test_put_ticket_price():
    with allure.step("Попытка вызвать метод PUT для уточения стоимости билета"):  # noqa
        response = ApiPage.put_ticket_price(
            origin_iata='IJK',
            destination_iata='MOW',
            depart_start='2025-08-01',
            depart_range=6
        )
    # Проверяем статус код
    assert response.status_code == 404


@allure.epic("API Tests")
@allure.description("Получение информации о билете без указания обязательного значения") # noqa
@allure.feature("Вывод список стоимость билетов без указания даты")
def test_price_matrix_without_depart_months():
    with allure.step("Получение цен без месяцев вылета"):
        response = ApiPage.get_price_no_depart_months()
    # Проверка статуса ответа
    assert response.status_code == 400
