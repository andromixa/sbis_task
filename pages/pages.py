import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import *


class BasePage:
    def __init__(self, browser, url, logger, timeout=5):
        self.browser = browser
        self.logger = logger
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.expected_size = 0
        self.download_dir = os.path.dirname(os.path.dirname(__file__))

    def open(self):
        self.logger.info(f'Открытие страницы {self.url}')
        self.browser.get(self.url)

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

    def element(self, locator):
        return self.browser.find_element(*locator)


class SbisMainPage(BasePage):
    def go_to_contacts_page(self):
        self.logger.info('Открытие меню "Контакты"')
        menu_link = self.element(SbisMainPageLocators.CONTACTS_LINK)
        menu_link.click()
        self.logger.info('Переход по ссылке на страницу "Контакты"')
        contacts_link = self.element(SbisMainPageLocators.MORE_OFFICES_LINK)
        contacts_link.click()

    def go_to_downloads_page(self):
        self.logger.info("Переход по ссылке на страницу 'Скачать'")
        download_link = self.element(SbisMainPageLocators.DOWNLOAD_PAGE_LINK)
        download_link.click()


class SbisContactsPage(BasePage):
    def go_to_tensor(self):
        self.logger.info('Переход по ссылке на главную страницу Тензор')
        tensor_banner = self.element(SbisContactsPageLocators.TENSOR_BANNER)
        tensor_banner.click()

    def should_be_right_region(self, expected_region, expected_city):
        self.logger.info(f'Проверка выбранного региона: {expected_region}, г.{expected_city}')
        region_name = self.element(SbisContactsPageLocators.REGION_IN_HEADER)
        assert region_name.text == expected_region, \
            f"Выбранный регион ({region_name.text}), не соответствует ожидаемому ({expected_region})"
        city_name = self.element(SbisContactsPageLocators.CITY_NAME_IN_CONTACTS)
        assert city_name.text == expected_city, \
            f"Выбранный город ({city_name.text}), не соответствует ожидаемому ({expected_city})"

    def choose_region(self, new_region):
        self.logger.info(f"Смена региона на {new_region}")
        region_menu_link = self.element(SbisContactsPageLocators.REGION_IN_HEADER)
        region_menu_link.click()
        region_popup = self.element(SbisContactsPageLocators.REGION_POPUP)
        new_region_link = region_popup.find_element(*SbisContactsPageLocators.get_region_link(new_region))
        self.browser.execute_script("arguments[0].click();", new_region_link)


class SbisDownloadPage(BasePage):
    def go_to_windows_plugin_tab(self):
        self.logger.info("Переход на нужную вкладку: Скачать - СБИС Плагин - Windows")
        plugin_tab = self.element(SbisDownloadPageLocators.PLUGIN_TAB)
        plugin_tab.click()
        windows_tab = self.element(SbisDownloadPageLocators.WINDOWS_TAB)
        windows_tab.click()

    def download_plugin(self):
        self.logger.info("Скачивание файла плагина")
        download_link = self.element(SbisDownloadPageLocators.DOWNLOAD_LINK)
        self.expected_size = float(download_link.text.split()[2])
        download_link.click()

    def should_be_downloaded(self, filename):
        self.logger.info(f"Проверка: скачался ли файл {filename}?")
        downloaded_file_path = os.path.join(self.download_dir, filename)
        for _ in range(60):
            if os.path.isfile(downloaded_file_path):
                break
            else:
                time.sleep(1)
        assert os.path.isfile(downloaded_file_path), "Файл не был скачан"

    def should_be_expected_size(self, filename):
        self.logger.info(f"Проверка: совпадает ли фактический размер файла {filename} с указанным на сайте?")
        downloaded_file_path = os.path.join(self.download_dir, filename)
        file_size = round(os.path.getsize(downloaded_file_path) / (1024 * 1024), 2)
        assert file_size == self.expected_size, \
            (f"Фактический размер скаченного файла ({file_size} Mb) не соответствует "
             f"ожидаемому значению ({self.expected_size} Mb)")

    def delete_file(self, filename):
        self.logger.info(f"Удаление файла {filename}")
        downloaded_file_path = os.path.join(self.download_dir, filename)
        try:
            os.remove(downloaded_file_path)
            self.logger.info(f"Файл {downloaded_file_path} успешно удалён.")
        except FileNotFoundError:
            self.logger.error(f"Файл {downloaded_file_path} не найден.")


class TensorMainPage(BasePage):
    def should_be_strength_in_people(self):
        self.logger.info('Проверка наличия блока "Сила в людях"')
        assert self.is_element_present(*TensorMainPageLocators.STRENGTH_IN_PEOPLE), \
            f"Раздел 'Сила в людях' не обнаружен на странице"

    def go_to_about(self):
        self.logger.info('Переход по ссылке на страницу О компании Тензор')
        about_link = self.element(TensorMainPageLocators.ABOUT_PAGE_LINK)
        about_link.click()


class TensorAboutPage(BasePage):
    def pics_should_have_equal_dims(self):
        self.logger.info('Проверка соответствия размеров изображений в блоке "Работаем"')
        pics = self.element(TensorAboutPageLocators.PICS_WORKING)
        assert len(set([(pic.get_attribute('width'), pic.get_attribute('height')) for pic in pics])) == 1, \
            f"Размеры изображений не совпадают"
