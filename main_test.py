import pytest
from pages.pages import *

MAIN_PAGE = 'https://sbis.ru/'


# @pytest.mark.skip(reason="DEBUGGING")
def test_go_to_tensor(browser, logger):
    logger.info(f"\tЗапуск теста: {test_go_to_tensor.__name__}")
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
    logger.info(f"\tКонец теста: {test_go_to_tensor.__name__}")


# @pytest.mark.skip(reason="DEBUGGING")
@pytest.mark.parametrize(
    'region, city', [
        ('Камчатский край', 'Петропавловск-Камчатский'),
        ("Пермский край", "Пермь")
    ], ids=["Камчатский край", "Пермский край"])
def test_change_region(browser, logger, region, city):
    logger.info(f"\tЗапуск теста: {test_change_region.__name__} ({region})")
    start_page = SbisMainPage(browser, MAIN_PAGE, logger)
    start_page.open()
    start_page.go_to_contacts_page()
    contacts_page = SbisContactsPage(browser, browser.current_url, logger)
    contacts_page.should_be_right_region('Тюменская обл.', 'Тюмень')
    contacts_page.choose_region(region)
    time.sleep(3)
    new_contacts_page = SbisContactsPage(browser, browser.current_url, logger)
    new_contacts_page.should_be_right_region(region, city)
    logger.info(f"\tКонец теста: {test_change_region.__name__} ({region})")


# @pytest.mark.skip(reason="DEBUGGING")
def test_app_download(browser, logger):
    logger.info(f"\tЗапуск теста: {test_app_download.__name__}")
    start_page = SbisMainPage(browser, MAIN_PAGE, logger)
    start_page.open()
    start_page.go_to_downloads_page()
    download_page = SbisDownloadPage(browser, browser.current_url, logger)
    download_page.go_to_windows_plugin_tab()
    download_page.download_plugin()
    download_page.should_be_downloaded("sbisplugin-setup-web.exe")
    download_page.should_be_expected_size("sbisplugin-setup-web.exe")
    download_page.delete_file("sbisplugin-setup-web.exe")
    logger.info(f"\tКонец теста: {test_app_download.__name__}")
