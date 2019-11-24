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
def loginPost(name, passwrd):
    driver.delete_all_cookies()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    username = driver.find_element_by_name("username")
    username.send_keys(name)
    password = driver.find_element_by_name("password")
    password.send_keys(passwrd)
    password.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.get("http://localhost:8000/admin/blog/post/add/")
    return True

def comment_input(author, body):
    driver.get("http://localhost:8000/blog/3/")
    driver.find_element_by_name("author").send_keys(author)
    driver.find_element_by_name("body").send_keys(body)
    driver.find_element_by_css_selector('button.btn.btn-primary').click()
    time.sleep(1)
    return True

def edituserinfo(name, passwrd, confirmpasswrd):
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys(name)

    password = driver.find_element_by_name("password1")
    password.clear()
    password.send_keys(passwrd)

    password1 = driver.find_element_by_name("password2")
    password1.clear()
    password1.send_keys(confirmpasswrd)
    time.sleep(1)

    return True

def update(user, FName, LName, email):

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys(user)

    first = driver.find_element_by_name("first_name")
    first.clear()
    first.send_keys(FName)

    last = driver.find_element_by_name("last_name")
    last.clear()
    last.send_keys(LName)

    mail = driver.find_element_by_name("email")
    mail.clear()
    mail.send_keys(email)

    driver.find_element_by_name("_save").click()
    time.sleep(1)

    return True

def updatePassword(passwrd1, passwrd2):
    pass1 = driver.find_element_by_name("password1")
    # pass1.clear()
    pass1.send_keys(passwrd1)
    pass2 = driver.find_element_by_name("password2")
    # pass2.clear()
    pass2.send_keys(passwrd2)
    pass2.send_keys(Keys.RETURN)
    time.sleep(1)


def post_input(title, body, value):
    post = driver.find_element_by_name("title")
    post.clear()
    post.send_keys(title)
    content = driver.find_element_by_name("body")
    content.clear()
    content.send_keys(body)
    time.sleep(1)
    category = Select(driver.find_element(By.XPATH, '//*[@id="id_categories"]'))
    category.select_by_value(value)
    time.sleep(1)
    driver.find_element_by_name("_save").click()
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
    #driver.close()
    
#test comments

def test_create_comment_valid():
    comment_input("Commentor 1", "ETI is hard")
    assert "ETI is hard" in driver.page_source
    time.sleep(1)


def test_invalid_author_blank():
    comment_input("", "no author")
    assert "Fill out this fields" in driver.page_source
    time.sleep(1)

def test_invalid_body_blank():
    comment_input("no body", "")
    assert "Fill out this fields" in driver.page_source
    time.sleep(1)

def test_invalid_all_blank():
    comment_input("", "")
    assert "Fill out this fields" in driver.page_source
    time.sleep(1)
    #driver.close()

#create new user
def test_createNewUser_NewUsername():
    login("yunteng", "19V38r00")
    driver.get("http://localhost:8000/admin/auth/user/add/")
    time.sleep(1)
    edituserinfo("newuser1", "B3stpass!", "B3stpass!")
    driver.find_element_by_name("_save").click()
    time.sleep(1)
    assert "was added successfully. You may edit it again below." in driver.page_source
    time.sleep(1)

#invalidNU
def test_createNU_ExistingUsername():
    driver.get("http://localhost:8000/admin/auth/user/add/")
    time.sleep(1)
    edituserinfo("yunteng", "B3stpass!", "B3stpass!")
    driver.find_element_by_name("_save").click()
    time.sleep(1)
    assert "Please correct the error below." in driver.page_source
    time.sleep(1)
    
    
#invalidPW
def test_createInvalidPW_NotSame():
    driver.get("http://localhost:8000/admin/auth/user/add/")
    time.sleep(1)
    edituserinfo("newuser2", "B3stpass!", "B3stpass!!!")
    driver.find_element_by_name("_save").click()
    time.sleep(1)
    assert "Please correct the error below." in driver.page_source
    time.sleep(1)

def test_createInvalidPW_under8():
    driver.get("http://localhost:8000/admin/auth/user/add/")
    time.sleep(1)
    edituserinfo("newuser2", "B3stpas", "B3stpas")
    driver.find_element_by_name("_save").click()
    time.sleep(1)
    assert "Please correct the error below." in driver.page_source
    time.sleep(1)

def test_createInvalidPW_Common():
    driver.get("http://localhost:8000/admin/auth/user/add/")
    time.sleep(1)
    edituserinfo("newuser2", "password", "password")
    driver.find_element_by_name("_save").click()
    time.sleep(1)
    assert "Please correct the error below." in driver.page_source
    time.sleep(1)

def test_createInvalidPW_Numerical():
    driver.get("http://localhost:8000/admin/auth/user/add/")
    time.sleep(1)
    edituserinfo("newuser2", "12345678", "12345678")
    driver.find_element_by_name("_save").click()
    time.sleep(1)
    assert "Please correct the error below." in driver.page_source
    time.sleep(1)
    driver.close()

#doesnt work
'''
def test_create_valid_post():
    loginPost("yunteng", "19V38r00")
    post_input("Test Post 1", "ETI", 1)
    time.sleep(1)
    assert "success" in driver.page_source
'''

#create an invalid post
#doesnt register index for category 
'''
def test_invalid_title_exists():
    login("yunteng", "19V38r00")
    post_input("Django", "abcdefg", 1)
    assert "error" in driver.page_source

def test_invalid_blank_title():
    login("yunteng", "19V38r00")
    post_input("", "abcdefg", 1)
    assert "error" in driver.page_source

def test_invalid_blank_body():
    login("yunteng", "19V38r00")
    post_input("Blankbody", "", 1)
    assert "error" in driver.page_source

def test_all_blank():
    login("yunteng", "19V38r00")
    post_input("", "", 1)
    assert "error" in driver.page_source'''
