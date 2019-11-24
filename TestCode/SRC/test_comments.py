'''import pytest
import os
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()

#functions that are used throughout
def comment_input(author, body):
    driver.get("http://localhost:8000/blog/3/")
    driver.find_element_by_name("author").send_keys(author)
    driver.find_element_by_name("body").send_keys(body)
    driver.find_element_by_css_selector('button.btn.btn-primary').click()
    return True



def test_create_comment_valid():
    comment_input("Commentor 1", "ETI is hard")
    assert "ETI is hard" in driver.page_source

def test_invalid_author_blank():
    comment_input("", "no author")
    assert "Fill in the fields" in driver.page_source

def test_invalid_body_blank():
    comment_input("no body", "")
    assert "Fill in the fields" in driver.page_source

def test_invalid_all_blank():
    comment_input("", "")
    assert "Fill in the fields" in driver.page_source
    driver.close()
    '''