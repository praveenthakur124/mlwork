from seleniumwire import webdriver
from time import sleep
from random import randint
from selenium.webdriver.chrome.options import Options


def signature(url):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(randint(10, 15))

    for request in driver.requests:
        if request.response:
            print(request.path, request.response.status_code, request.response.headers['Content-Type'])

    driver.quit()


signature('https://www.tiktok.com/en/trending')


