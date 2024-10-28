from selenium.webdriver.common.by import By

CONTACTS_LINK = (By.XPATH, "//div[contains(text(), 'Контакты')]")
MORE_OFFICES_LINK = (By.XPATH, "//span[contains(text(), 'офис в России')]")
TENSOR_BANNER = (By.XPATH, "//div[@class='sbisru-Contacts__border-left sbisru-Contacts__border-left--border-xm "
                           "pl-20 pv-12 pl-xm-0 mt-xm-12']/a[@title[contains(., 'tensor.ru')]]")
STRENGTH_IN_PEOPLE = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
ABOUT_PAGE_LINK = (By.XPATH, "//p[@class='tensor_ru-Index__card-text']/a[@href = '/about']")
PICS_WORKING = (By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']/"
                          "div[@class='s-Grid-container']//img")
