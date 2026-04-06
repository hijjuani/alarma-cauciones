import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import URL, LOAD_WAIT

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.get(URL)
    time.sleep(10)
    return driver

def get_tasas(driver):
    driver.refresh()
    time.sleep(LOAD_WAIT)

    html = driver.page_source
    tasas = re.findall(r'(\d{1,3}[.,]\d{1,2})\s*%', html)
    tasas = [float(x.replace(",", ".")) for x in tasas]

    if len(tasas) >= 14:
        return {
            "ars_1": tasas[4],
            "usd_1": tasas[5],
            "ars_7": tasas[12],
            "usd_7": tasas[13],
        }

    return None