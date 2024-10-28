import logging
from selenium.common.exceptions import (
    NoSuchElementException,
    NoAlertPresentException,
    TimeoutException,
)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import *


class BasePage:
    def __init__(self, browser, url, logger, timeout=5):
        self.browser = browser
        self.logger = logger
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.logger.info(f'Открытие страницы {self.url}')
        self.browser.get(self.url)

    def scroll_down(self, pxls=100):
        self.logger.info(f'Прокрутка страницы на {pxls} пикселей вниз')
        self.browser.execute_script(f"window.scrollBy(0, {pxls});")

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except NoSuchElementException:
            return False
        return True

    def move_to_new_page(self):
        self.logger.info(f'Переход на новую вкладку')
        window_handles = self.browser.window_handles
        self.browser.switch_to.window(window_handles[-1])

    def url_should_be(self, expected_url):
        self.logger.info(f'Проверка соответствия реального URL {self.browser.current_url} ожидаемому {expected_url}')
        assert self.browser.current_url == expected_url, \
            f"Адрес страницы ({self.browser.current_url}) не соответствует ожидаемому: {expected_url}"


class SbisMainPage(BasePage):
    def go_to_contacts_page(self):
        self.logger.info('Открытие меню "Контакты"')
        menu_link = self.browser.find_element(*CONTACTS_LINK)
        menu_link.click()
        self.logger.info('Переход по ссылке на страницу "Контакты"')
        contacts_link = self.browser.find_element(*MORE_OFFICES_LINK)
        contacts_link.click()


class SbisContactsPage(BasePage):
    def go_to_tensor(self):
        self.logger.info('Переход по ссылке на главную страницу Тензор')
        tensor_banner = self.browser.find_element(*TENSOR_BANNER)
        tensor_banner.click()


class TensorMainPage(BasePage):
    def should_be_strength_in_people(self):
        self.logger.info('Проверка наличия блока "Сила в людях"')
        assert self.is_element_present(*STRENGTH_IN_PEOPLE), \
            f"Раздел 'Сила в людях' не обнаружен на странице"

    def go_to_about(self):
        self.logger.info('Переход по ссылке на страницу О компании Тензор')
        about_link = self.browser.find_element(*ABOUT_PAGE_LINK)
        about_link.click()


class TensorAboutPage(BasePage):
    def pics_should_have_equal_dims(self):
        self.logger.info('Проверка соответствия размеров изображений в блоке "Работаем"')
        pics = self.browser.find_elements(*PICS_WORKING)
        assert len(set([(pic.get_attribute('width'), pic.get_attribute('height')) for pic in pics])) == 1, \
            f"Размеры изображений не совпадают"
