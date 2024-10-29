from selenium.webdriver.common.by import By


class SbisMainPageLocators:
    CONTACTS_LINK = (By.XPATH, "//div[contains(text(), 'Контакты')]")
    MORE_OFFICES_LINK = (By.XPATH, "//span[contains(text(), 'офис в России')]")
    DOWNLOAD_PAGE_LINK = (By.XPATH, "//a[@href = '/download']")


class SbisContactsPageLocators:
    TENSOR_BANNER = (By.XPATH, "//div[@class='sbisru-Contacts__border-left sbisru-Contacts__border-left--border-xm "
                               "pl-20 pv-12 pl-xm-0 mt-xm-12']/a[@title[contains(., 'tensor.ru')]]")
    REGION_IN_HEADER = (By.XPATH, "//div[@class='sbis_ru-container sbisru-Contacts__relative']//"
                                  "span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    CITY_NAME_IN_CONTACTS = (By.CSS_SELECTOR, "#city-id-2")
    REGION_POPUP = (By.XPATH, "//*[@id='popup']")

    @staticmethod
    def get_region_link(region):
        return By.XPATH, f"//span[contains(text(),'{region}')]"


class SbisDownloadPageLocators:
    PLUGIN_TAB = (By.XPATH, "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']")
    WINDOWS_TAB = (By.XPATH, "//span[@class='sbis_ru-DownloadNew-innerTabs__title "
                             "sbis_ru-DownloadNew-innerTabs__title--default' and text()='Windows']")
    DOWNLOAD_LINK = (By.XPATH, "//a[contains(text(),'Скачать (Exe')]")


class TensorMainPageLocators:
    STRENGTH_IN_PEOPLE = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    ABOUT_PAGE_LINK = (By.XPATH, "//p[@class='tensor_ru-Index__card-text']/a[@href = '/about']")


class TensorAboutPageLocators:
    PICS_WORKING = (By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']"
                              "div[@class='s-Grid-container']//img")


