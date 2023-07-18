from PageObject.Hashtag_POM import CareerPage
from Utilities.readConfigFile import Read_values
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class TestCareerPage:

    get_name = Read_values.getName()
    get_email = Read_values.getEmail()
    get_phone = Read_values.getPhone()
    get_descrp = Read_values.getDescrp()



    def test_TC001(self, setup):       #Check if the URL is correct and working.
        self.driver = setup

        actual_url = self.driver.current_url
        expected_url = 'https://www.hashtag-ca.com/careers/apply?jobCode=QAE001'

        print("Actual URL:", actual_url)
        print("Expected URL:", expected_url)

        if expected_url == actual_url:
            assert True
            print('URL is correct.')

        else:
            assert False
            print('URL is not correct.')

        self.driver.close()



    def test_TC018(self, setup):         # Validate submitting the application form with blank inputs in 'Join us' section.
        self.driver = setup

        self.attribute = CareerPage(self.driver)

        self.attribute.click_apply_button()

        error_ele = self.attribute.error_message()
        error_msg = error_ele.text
        expected_error_msg = 'something went wrong! please try again later'

        print("Actual Error Message:", error_msg)
        print("Expected Error Message:", expected_error_msg)

        if error_msg == expected_error_msg:
            assert True
            print('The application could not submit blank form. Test Passed.')

        else:
            assert False
            print('Test Failed.')

        self.driver.close()



    def test_TC027(self, setup):       # Validate submitting the application form with valid inputs.
        self.driver = setup

        self.attribute = CareerPage(self.driver)

        self.attribute.Name(self.get_name)
        self.attribute.Email(self.get_email)
        self.attribute.Phone(self.get_phone)
        time.sleep(3)
        self.attribute.Resume()
        time.sleep(5)
        self.attribute.descript_field(self.get_descrp)
        self.attribute.click_apply_button()
        time.sleep(5)

        error_ele = self.attribute.error_message()
        error_msg = error_ele.text
        expected_error_msg = 'something went wrong! please try again later'

        print("Actual Error Message:", error_msg)
        print("Expected Error Message:", expected_error_msg)

        if error_msg == expected_error_msg:
            assert False
            print('Application could not be submitted. Test Failed.')

        else:
            assert True
            print('Application submitted successfully. Test Passed.')

        self.driver.close()



    def test_TC029(self, setup):      #Validate Clicking on the 'Hashtag' logo gets you to the Home Page.

        self.driver = setup

        self.attribute = CareerPage(self.driver)

        self.attribute.logo_click()

        if self.attribute.homePage_element().is_displayed():
            print("Successfully arrived at the home page!")
        else:
            print("Failed to navigate to the home page.")


        self.driver.close()







