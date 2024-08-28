from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.param import kinopoisk_ui_url
import allure

class Kinopoisk:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(kinopoisk_ui_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step("Поиск фильма по названию")
    def search_film(self):
        WebDriverWait (self.driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'styles_root__W1oqS')]"))
        )
        self.driver.find_element(By. XPATH, "//button[contains(@class, 'styles_root__EjoL7')]").click()
        self.driver.find_element(By. XPATH, "//input[@name='kp_query']").send_keys("Майор Гром: Чумной Доктор")
        self.driver.find_element(By. XPATH, "//button[contains(@aria-label, 'Найти') and contains (@class, 'styles_root')]").click()
        self.driver.find_element(By. XPATH, "//a[normalize-space(text())='Майор Гром: Чумной Доктор']").click()
    
    @allure.step("Проверка найденного фильма")
    def res_search_film(self):
        return self.driver.find_element(By. XPATH, "//span[normalize-space(text())='Майор Гром: Чумной Доктор (2021)']").text 
    
    @allure.step("Просмотр фильмов для покупки билетов в кино")
    def ticket(self):
        self.driver.find_element(By. XPATH, "//div[contains(@class, 'styles_sticky__mDnbt')]//a[normalize-space(text())='Билеты в кино']").click()
        self.driver.find_element(By. XPATH, "//a[normalize-space(text())='Российские']").click()
    
    @allure.step("Проверка билетов в кино")
    def res_ticket(self):
        return self.driver.find_element(By. XPATH, "//h1[normalize-space(text())='Билеты в кино']").text 
    
    @allure.step("Поиск актера")
    def search_actor(self):
        self.driver.find_element(By. XPATH, "//input[@name='kp_query']").send_keys("Павел Прилучный")
        self.driver.find_element(By. XPATH, "//button[contains(@aria-label, 'Найти') and contains (@class, 'styles_root')]").click()
    
    @allure.step("Проверка найденного актера")
    def res_search_actor(self):
        return self.driver.find_element(By. XPATH, "//h1[normalize-space(text())='Павел Прилучный']").text

    @allure.step("Переход к просмотру спортивных мероприятий")
    def sport(self):
        self.driver.find_element(By. XPATH, "//div[contains(@class, 'styles_sticky__mDnbt')]//a[normalize-space(text())='Спорт']").click()

    @allure.step("Расширенный поиск")
    def full_search(self):
        self.driver.find_element(By. XPATH, "//a[contains(@aria-label, 'Расширенный поиск')]").click()
        self.driver.find_element(By. XPATH, "//input[@id='find_film']").send_keys("Майор Гром: Чумной Доктор")
        self.driver.find_element(By. XPATH, "//input[@id='year']").send_keys("2021") 
        self.driver.find_element(By. XPATH, "//input[@class='text el_9']").send_keys("Тихон Жизневский") 
        self.driver.find_element(By. XPATH, " //input[@class='el_18 submit nice_button']").click()
        self.driver.find_element(By. XPATH, "//a[normalize-space(text())='Майор Гром: Чумной Доктор']").click() 
    
    @allure.step("Проверка результатов расширенного поиска")
    def res_full_search(self):
        return self.driver.find_element(By. XPATH, "//span[normalize-space(text())='Майор Гром: Чумной Доктор (2021)']").text

