from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import sys
from pyvirtualdisplay import Display

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('C:/driver',
                          chrome_options=chrome_options)


def getDriverHttp(url):
    driver.get(url)
    iframe = driver.find_elements_by_tag_name('iframe')[1]
    driver.switch_to.frame(iframe)                          # 最重要的一步
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup





if __name__ == '__main__':
    url = getDriverHttp(u'https://www.cnbc.com/quotes/?symbol=AAPL&tab=profile')
# path = getVideoUrl(url==sys.argv[1])
    print(url)


from urllib import parse

src = driver.find_element_by_name("quote_profile_iframe").get_attribute("src")
url = parse.urljoin('https://www.cnbc.com/quotes/?symbol=AAPL&tab=profile', src)

driver.get(url)
print(driver.page_source)