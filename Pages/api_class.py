import requests

class Kinopoisk_Api:
    def __init__(self, url):
        self.url = url

    def search_film_id(self, id):
        headers = {
        "accept": "application/json",
        "X-API-KEY": "N0GKKMM-82CMAP1-PA8MZS0-VNEF6KE"
        }       
        response = requests.get(self.url+'/movie/' + str(id), headers=headers)
        return response
    
