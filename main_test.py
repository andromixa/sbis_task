import time
from pages.pages import *
from pages.locators import PICS_WORKING

MAIN_PAGE = 'https://sbis.ru/'


def test_go_to_tensor(browser, logger):
    logger.info(f"Запуск теста: {test_go_to_tensor.__name__}")
    start_page = SbisMainPage(browser, MAIN_PAGE, logger)
    start_page.open()
    start_page.go_to_contacts_page()
    contacts_page = SbisContactsPage(browser, browser.current_url, logger)
    contacts_page.go_to_tensor()
    contacts_page.move_to_new_page()
    tensor_main_page = TensorMainPage(browser, browser.current_url, logger)
    tensor_main_page.should_be_strength_in_people()
    tensor_main_page.go_to_about()
    tensor_main_page.url_should_be('https://tensor.ru/about')
    about_page = TensorAboutPage(browser, browser.current_url, logger)
    about_page.pics_should_have_equal_dims()

    time.sleep(10)
