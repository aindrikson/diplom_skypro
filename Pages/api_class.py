import requests
import allure

class Kinopoisk_Api:
    def __init__(self, url):
        self.url = url
    
    @allure.step("api. Получение информации о фильме по {id}")
    def search_film_id(self, id, headers):
        response = requests.get(self.url+'/movie/' + str(id), headers=headers)
        return response
    
    @allure.step("api. Получение информации о фильме по названию")
    def search_film_name(self, headers, name):
        my_params = {
            'page' : '1',
            'limit' : '1',
            'query' : name
         }
        response = requests.get(self.url+'/movie/'+'/search/', params = my_params, headers=headers)
        return response
    
    @allure.step("api. Получение информации о фильме по году выхода")
    def search_film_date(self, date, headers):
        my_params = {
            'page' : '1',
            'limit' : '10',
            'year' : date
         }
        response = requests.get(self.url+'/movie/'+'/search/', params = my_params, headers=headers)
        return response
    
    @allure.step("api. Получение информации об актере по {id}")
    def search_actor_id(self, id, headers):
        response = requests.get(self.url+'/person/' + str(id), headers=headers)
        return response
    
    @allure.step("api. Получение информации об актере по имени и фамилии")
    def search_actor_name(self, headers, name):
        my_params = {
            'page' : '1',
            'limit' : '10',
            'query' : name
         }
        response = requests.get(self.url+'/person/'+'/search/', params = my_params, headers=headers)
        return response
    