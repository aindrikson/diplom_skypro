from Pages.ui_class import Kinopoisk
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import allure

driver = webdriver.Firefox(
service=FirefoxService(GeckoDriverManager().install()))

@allure.epic("UI Class")
@allure.severity(severity_level='normal')
@allure.title("Поиск фильма")
@allure.description("Поиск фильма и последующая проверка найденного фильма")
@allure.feature('Тест 1')
def test_search_film():
 with allure.step("Открытие интернет-сервиса и поиск фильма"):
    ui_class = Kinopoisk(driver)
    ui_class.search_film()
 with allure.step("Проверка найденого фильма"):
    res = ui_class.res_search_film()
    assert res == "Майор Гром: Чумной Доктор (2021)"

@allure.epic("UI Class")
@allure.severity(severity_level='normal')
@allure.title("Поиск билетов")
@allure.description("Поиск билетов в кино для покупки")
@allure.feature('Тест 2')
def test_ticket():
 with allure.step("Открытие интернет-сервиса и переход в раздел"):
    ui_class = Kinopoisk(driver)
    ui_class.ticket()
 with allure.step("Проверка перехода в раздел"):
    res = ui_class.res_ticket()
    assert res == "Билеты в кино"

@allure.epic("UI Class")
@allure.severity(severity_level='normal')
@allure.title("Поиск актера")
@allure.description("Поиск актера и проверка найденного актера")
@allure.feature('Тест 3')
def test_search_actor():
 with allure.step("Открытие интернет-сервиса и поиск актера"):
    ui_class = Kinopoisk(driver)
    ui_class.search_actor()
 with allure.step("Проверка найденного актера"):
    res = ui_class.res_search_actor()
    assert res == "Павел Прилучный"

@allure.epic("UI Class")
@allure.severity(severity_level='normal')
@allure.title("Переход в раздел Спорт")
@allure.description("Переход в раздел Спорт и проверка url раздела")
@allure.feature('Тест 4')
def test_sport():
 with allure.step("Открытие интернет-сервиса и переход в раздел Спорт"):
    ui_class = Kinopoisk(driver)
    ui_class.sport()
 with allure.step("Проверка url"):
    url = driver.current_url
    assert url == "https://hd.kinopoisk.ru/sport/"

@allure.epic("UI Class")
@allure.severity(severity_level='normal')
@allure.title("Расширенный поиск")
@allure.description("Переход в расширенный поиск, последующий поиск фильма и проверка найденного фильма")
@allure.feature('Тест 5')
def test_full_search():
 with allure.step("Открытие интернет-сервиса и переход в расширенный поиск, поиск фильма"):
    ui_class = Kinopoisk(driver)
    ui_class.full_search()
 with allure.step("Проверка найденного фильма"):
    res = ui_class.res_full_search()
    assert res == "Майор Гром: Чумной Доктор (2021)"