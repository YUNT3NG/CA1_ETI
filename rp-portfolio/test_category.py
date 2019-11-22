import pytest
import os
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#login to a superuser first
def test_create_new_valid_params():
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    username = driver.find_element_by_name("username")
    username.send_keys("yunteng")
    password = driver.find_element_by_name("password")
    password.send_keys("19V38r00")
    password.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a').click()
    catName = driver.find_element_by_name("name")
    catName.send_keys("TestCat1")
    driver.find_element_by_name("_save").click()
    assert "Select category to change | Django site admin" in driver.title
