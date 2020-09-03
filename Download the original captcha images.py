from selenium import webdriver
from urllib.request import urlretrieve
from selenium.common.exceptions import NoSuchElementException,TimeoutException,ElementNotInteractableException


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


chromedriver_location = 'your chromedriver location'
url_amazon_item = 'the url of item that you wish to scrap'
path_save = 'location that you want to save the original captcha image'

driver = webdriver.Chrome(chromedriver_location)
driver.get(url_amazon_item)

"""
//div[@class='a-box a-alert a-alert-info a-spacing-base'] : xpath of the capthca in amazon website
"""

if check_exists_by_xpath("//div[@class='a-box a-alert a-alert-info a-spacing-base']") == True:
    src = driver.find_elements_by_tag_name('img')[0].get_attribute('src')
    urlretrieve(src,path_save+'captcha.png')
else:
    "continue your processing"

