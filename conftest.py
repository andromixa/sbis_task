import logging

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope='session')
def logger():
    # Создание логгера
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Создание обработника для записи в файл
    file_handler = logging.FileHandler('test_log.log')
    file_handler.setLevel(logging.INFO)

    # Создание обработника для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Формат логов
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Добавление обработчиков к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    yield logger
