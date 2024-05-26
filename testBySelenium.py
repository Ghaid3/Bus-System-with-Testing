# -*- coding: utf-8 -*-
"""
COMP4402/ Spring 23/ Project/Part4/Dynamic Testing
Ruaa Alrashdi - ID:129245
Ghaidaa Alrawahi - ID: 131760
Submitted to: prof. Yocef Baghdadi 

-- Selenium Part --

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleSearch(unittest.TestCase):
    

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")
    
    #check if the search button clickable
    def test_search_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")) )
    #test if the search field enable
    def test_search_inputText(self):
        enable = self.driver.find_element(By.NAME, 'q').is_enabled
        self.assertTrue(enable)
    def test_search_in_Google(self):
        # test the input text
        self.driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys("Selenium")
        # test different buttons
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
        self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/a/h3/span').click()
        self.driver.implicitly_wait(16)
        self.driver.find_element(By.XPATH, '/html/body/div/main/section[2]/div/div/div[1]/div/div[2]/div/a').click()
        # get the title of the page to test it with the actaul title
        expected_title = self.driver.title
        print("The expected title: ",expected_title)
        self.assertEqual("WebDriver | Selenium", expected_title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()