import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture()
def setup():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    driver = webdriver.Chrome()  # options=chrome_options
    driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
    driver.maximize_window()
    return driver



# -------------------------------------for cross browser testing---------------------------------
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture()
# def setup(browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#         driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
#         print("Opening Chrome browser.")
#
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#         driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
#         print("Opening Firefox browser.")
#
#     elif browser == "edge":
#         driver = webdriver.Edge()
#         driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
#         print("Opening Edge browser.")
#
#     else:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")
#         print("Opening Chrome browser in non-gui mode.")
#
#     driver.maximize_window()
#     return driver
