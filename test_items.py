import pytest
import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_user_see_button_language(browser):
    browser.get(link)
    time.sleep(15) 
    addbutton = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    assert addbutton, "Button is absent"
    