from page.MainPage import MainPage
import pytest  # noqa
import allure


@allure.epic("Поиск билетов")
@allure.feature("Поиск с пустым полем 'Куда'")
@allure.description("Тесты на проверку поведения формы поиска на странице Aviasales")  # noqa
def test_search_with_empty_to(driver):
    with allure.step("Открываем страницу и оставляем поля 'Куда' пустым"): # noqa
        page = MainPage(driver)
        page.open()
        assert driver.find_element(*page.to_input).get_attribute('value') == ''
    with allure.step("Нажимаем поиск и проверяем, что URL не изменился"):
        page.click_search()
        assert driver.current_url.startswith("https://www.aviasales.ru")


@allure.epic("Поиск билетов")
@allure.feature("Поиск с пустым полем 'Дата вылета'")
@allure.description("Проверка поведения формы при пустом поле 'Дата вылета'.")
def test_search_with_empty_departure_date(driver):
    with allure.step("Открываем страницу и заполняем поле 'Куда'"):
        page = MainPage(driver)
        page.open()
        to_go = "Москва"
        page.set_to(to_go)
    with allure.step("Проверяем, что поле 'Дата вылета' пустое"):
        assert driver.find_element(*page.departure_date_input).get_attribute('value') == '' # noqa
    with allure.step("Нажимаем поиск и проверяем, что URL не изменился"):
        page.click_search()
        assert driver.current_url.startswith("https://www.aviasales.ru")


@allure.epic("Поиск билетов")
@allure.feature("Поиск с указанием невалидных символов")
@allure.description("Проверка поиска со специальными символами в поле 'Куда'.")
def test_search_with_special_symbols_in_to_field(driver):
    with allure.step("Открываем страницу и вводим спецсимволы в поле 'Куда'"):
        page = MainPage(driver)
        page.open()
        special_symbols = "!@#$%^&*()_+[]{}|;:'\",.<>/?`~"
        page.set_to(special_symbols)
    with allure.step("Выполняем поиск и проверяем содержимое поля 'Куда'"):
        page.click_search()
    to_value = driver.find_element(*page.to_input).get_attribute('value')
    assert to_value == special_symbols


@allure.epic("Поиск билетов")
@allure.feature("Поиск с указанием невалидных символов")
@allure.description("Проверка поиска с указанием 15 цифр в поле 'Куда'")
def test_search_15_numbers(driver):
    with allure.step("Открываем страницу и вводим 15 цифр в поле 'Куда'"):
        page = MainPage(driver)
        page.open()
        numbers = "123456789987654"
        page.set_to(numbers)
    with allure.step("Нажимаем поиск и проверяем, что URL не изменился"):
        page.click_search()
        assert driver.current_url.startswith("https://www.aviasales.ru")


@allure.epic("Поиск билетов")
@allure.feature("Поиск с указанием невалидных символов")
@allure.description("Проверка поиска с указанием 1 цифры в поле 'Куда'")
def test_search_one_numbers(driver):
    with allure.step("Открываем страницу и вводим число в поле 'Куда'"):
        page = MainPage(driver)
        page.open()
        numbers = "5"
        page.set_to(numbers)
    with allure.step("Нажимаем поиск и проверяем значение поля 'Куда'"):
        page.click_search()
        to_value = driver.find_element(*page.to_input).get_attribute('value')
        assert to_value == numbers
