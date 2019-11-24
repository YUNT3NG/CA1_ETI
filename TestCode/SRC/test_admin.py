'''import pytest
import os
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()

#login to a superuser first
def test_ErrorLogin():
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    username = driver.find_element_by_name("username")
    username.send_keys("yunteng123")
    password = driver.find_element_by_name("password")
    password.send_keys("19V38r00")
    password.send_keys(Keys.RETURN)

def test_Login():
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    username = driver.find_element_by_name("username")
    username.send_keys("yunteng")
    password = driver.find_element_by_name("password")
    password.send_keys("19V38r00")
    password.send_keys(Keys.RETURN)
    #driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a').click()
    #catName = driver.find_element_by_name("name")
    #catName.send_keys("TestCat1")
    #driver.find_element_by_name("_save").click()
    #return driver.find_element(By.XPATH, '//head//title/text()')

def test_CreateCategory():
    driver.get("http://localhost:8000/admin/blog/category/add/")
    username = driver.find_element_by_name("username")
    username.send_keys("yunteng")
    password = driver.find_element_by_name("password")
    password.send_keys("19V38r00")
    password.send_keys(Keys.RETURN)
    #catName = driver.find_element(By.XPATH, '//body/div/div[3]/div/form/div/fieldset/div/div/input"]')
    catName = driver.find_element_by_name("name")
    catName.send_keys("testCat1")
    driver.find_element_by_name("_save").click()
    doc = driver.find_element(By.XPATH,"//*[@id="id_name"]").send_keys('Facts')
    doc =  driver.find_element(By.XPATH"//*[@id="category_form"]/div/div/input[1]")
    doc.click()
   # return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")
   '''