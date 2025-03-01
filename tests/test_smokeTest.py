# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSmokeTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_smokeTest(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(974, 1057)
    self.driver.find_element(By.CSS_SELECTOR, ".header-top").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".header-top").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-title > h1")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, "#hamburger-equiv > img").click()
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    self.driver.set_window_size(1200, 1600)
    elements = self.driver.find_elements(By.LINK_TEXT, "Directory")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us").click()
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("gfd")
    self.driver.find_element(By.NAME, "lname").click()
    self.driver.find_element(By.NAME, "lname").send_keys("gfd")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("fdg")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("fdg")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("dsa@")
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("gfd")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("fdg")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".errorMessage")))
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 img")
    assert len(elements) > 0
    self.driver.close()
  
