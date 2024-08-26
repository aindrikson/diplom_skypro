from Pages.api_class import Kinopoisk_Api
import json
import pytest
import requests
import allure

api = Kinopoisk_Api('https://api.kinopoisk.dev/v1.4')
        
headers = {
"accept": "application/json",
"X-API-KEY": "N0GKKMM-82CMAP1-PA8MZS0-VNEF6KE"
}    

@allure.epic("Films")
@allure.severity(severity_level='normal')
@allure.title("Получение фильма по id")
@allure.description("Получение информации о фильме по id и его проверка")
@allure.feature('Тест 1')
def test_search_film_id():
 with allure.step("Получить фильм по id"):
    res = api.search_film_id(4742878, headers)
    film_id = res.json()['id'][0]
 with allure.step("Проверка id полученного фильма"):
    assert film_id == "4742878"
 with allure.step("Проверка статус кода"):
    assert res.status_code == 200

@allure.epic("Films")
@allure.severity(severity_level='normal')
@allure.title("Получение фильма по названию")
@allure.description("Получение информации о фильме по названию и его проверка")
@allure.feature('Тест 2')
def test_search_film_name():
 with allure.step("Получить фильм по названию"):
    res = api.search_film_name(headers, 'Один дома')
    film_name = res.json()['docs'][0]['name']
 with allure.step("Проверка названия полученного фильма"):
    assert film_name == "Один дома"
 with allure.step("Проверка статус кода"):
    assert res.status_code == 200

@allure.epic("Films")
@allure.severity(severity_level='normal')
@allure.title("Получение фильма по году выхода")
@allure.description("Получение информации о фильме по году выхода и его проверка")
@allure.feature('Тест 3')
def test_search_film_date():
 with allure.step("Получение фильма по дате выхода"):
    resp = api.search_film_date(2021, headers)
    response = resp.json()['dosc'][0]['year']
 with allure.step("Проверка года выхода фильма"):
    assert response == 2021
 with allure.step("Проверка статус кода"):
    assert resp.status_code == 200

@allure.epic("Actor")
@allure.severity(severity_level='normal')
@allure.title("Получение информации об актере по id")
@allure.description("Получение информации об актере по id и его проверка")
@allure.feature('Тест 4')
def test_search_actor_id():
 with allure.step("Получение информации об актере по id"):
    res = api.search_actor_id(1775081, headers)
    actor_id = res.json()[0]['id']
 with allure.step("Проверка id актера"):
    assert actor_id == "1775081"
 with allure.step("Проверка статус кода"):
    assert res.status_code == 200

@allure.epic("Actor")
@allure.severity(severity_level='normal')
@allure.title("Получение информации об актере по имени и фамилии")
@allure.description("Получение информации об актере по имени и фамилии, и его проверка")
@allure.feature('Тест 5')
def test_search_actor_name():
 with allure.step("Получение информации об актере по имени и фамили"):
    res = api.search_film_name(headers, 'Тихон Жизневский')
    actor_name = res.json()['docs'][0]['name']
 with allure.step("Првоерка имени и фамилии актера"):
    assert actor_name == "Тихон Жизневский"
 with allure.step("Проверка статус кода"):
    assert res.status_code == 200