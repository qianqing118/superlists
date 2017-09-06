# -*- coding: utf-8 -*-
__author__ = 'qianqing'

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title

