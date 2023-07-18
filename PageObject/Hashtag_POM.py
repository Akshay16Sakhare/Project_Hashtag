from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class CareerPage():

    name_field = (By.NAME, "name")
    email_field = (By.NAME, "email")
    phone_field = (By.NAME, "phone")
    resume_field = (By.ID, "inputFile")
    description_field = (By.XPATH, "//textarea[@placeholder='Briefly Describe Yourself']")
    apply_button = (By.XPATH, '//*[@id="contact-form"]/div/div[7]/div/button[1]')
    error_msg = (By.XPATH, "//p[normalize-space()='something went wrong! please try again later']")
    logo = (By.ID, "logo")
    homePage_ele = (By.ID, "home-main")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 8)

    def Name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def Email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def Phone(self, number):
        self.driver.find_element(*self.phone_field).send_keys(number)

    def Resume(self):
        choose_file = self.wait.until(EC.visibility_of_element_located(self.resume_field))
        choose_file.send_keys(r"C:\Users\Admin\PycharmProjects\Project_Has#tag\Resume.pdf")

    def descript_field(self, content):
        element = self.wait.until(EC.visibility_of_element_located(self.description_field))
        self.driver.execute_script("arguments[0].click();", element)
        element.send_keys(content)

    def click_apply_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.apply_button))
        self.driver.execute_script("arguments[0].click();", button)


    def error_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.error_msg))
        return message

    def logo_click(self):
        logo_ele = self.driver.find_element(*self.logo)
        logo_ele.click()

    def homePage_element(self):
        return self.wait.until(EC.visibility_of_element_located((self.homePage_ele)))



