from Pages.api_class import Kinopoisk_Api
import pytest
import requests

api = Kinopoisk_Api('https://api.kinopoisk.dev/v1.4')

def test_search_film_id():
    res = api.search_film_id("4742878")

    assert res["id"] == '4742878