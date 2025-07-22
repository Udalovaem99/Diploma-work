from selenium.webdriver.common.by import By
import pytest  # noqa
import allure


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = "https://www.aviasales.ru"
        self.to_input = (By.CSS_SELECTOR, "#avia_form_destination-input")
        self.departure_date_input = (By.CSS_SELECTOR, '[data-test-id="start-date-field"]')  # noqa
        self.return_date_input = (By.CSS_SELECTOR, '[data-test-id="end-date-value"]')  # noqa
        self.search_button = (By.CSS_SELECTOR, '[data-test-id="form-submit"]')

    @allure.step("Открыть сайт")
    def open(self):
        """
        Открывает страницу Aviasales
        """
        self.driver.get(self.url)

    @allure.step("Город вылета")
    def set_to(self, value):
        """
        Выбор города вылета.
        """
        elem = self.driver.find_element(*self.to_input)
        elem.clear()
        elem.send_keys(value) 

    @allure.step("Указать дату вылета")
    def set_departure_date(self, value):
        """
        ВЫбор даты вылета.
        """
        elem = self.driver.find_element(*self.departure_date_input)
        elem.clear()
        elem.send_keys(value)

    @allure.step("Указать дату прилета")
    def set_return_date(self, value):
        """
        Выбор даты прилета.
        """
        elem = self.driver.find_element(*self.return_date_input)
        elem.clear()
        elem.send_keys(value)

    @allure.step("Нажать поиск")
    def click_search(self):
        """
        Нажитие на кнопку поиск.
        """
        self.driver.find_element(*self.search_button).click()
