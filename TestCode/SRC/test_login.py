import pytest
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()

#functions to be used again
def login(name, passwrd):
    driver.delete_all_cookies()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    username = driver.find_element_by_name("username")
    username.send_keys(name)
    password = driver.find_element_by_name("password")
    password.send_keys(passwrd)
    password.send_keys(Keys.RETURN)
    time.sleep(1)
    return True

@pytest.mark.parametrize("adminpage", [
("http://localhost:8000/admin/"),
("http://localhost:8000/admin/auth/group/"),
("http://localhost:8000/admin/auth/group/add/"),
("http://localhost:8000/admin/auth/user/"),
("http://localhost:8000/admin/auth/user/add/"),
("http://localhost:8000/admin/blog/category/"),
("http://localhost:8000/admin/blog/category/add/"),
("http://localhost:8000/admin/blog/post/"),
("http://localhost:8000/admin/blog/post/add/"),
])
def test_admin_pages_access(adminpage):
    driver.get(adminpage)
    assert "Log in | Django site admin" in driver.title

@pytest.mark.parametrize("allpages", [
("http://localhost:8000/projects/"),
("http://localhost:8000/blog/"),
("http://localhost:8000/blog/3/"),
])
def test_access_all_pages(allpages):
    driver.get(allpages)
    assert driver.current_url == allpages

def test_view_login_page():
    driver.delete_all_cookies()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    assert "Log in | Django site admin" in driver.title

def test_wrong_password():
    login("yunteng", "wrongpassword")
    assert "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." in driver.page_source

def test_wrong_username():
    login("wrongusername", "19V38r00")
    assert "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." in driver.page_source

def test_username_doesnt_exist():
    login("usernil", "19V38r00")   
    assert "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." in driver.page_source


@pytest.mark.parametrize("a, b", [
("yunteng", "19V38r00"),
("user1", "user1user1"),
])
def test_correct_username_password(a,b):
    driver.get("http://localhost:8000/admin/logout/")
    time.sleep(1)
    login(a,b)
    assert driver.current_url == "http://localhost:8000/admin/"
    time.sleep(1)

def test_logout():
    time.sleep(1)
    driver.get("http://localhost:8000/admin/logout/")
    assert "Thanks for spending some quality time with the Web site today." in driver.page_source
    driver.close()
    
