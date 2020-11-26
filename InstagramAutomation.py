# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:01:31 2020


"""
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

user = ['username','username']
message_ = ("final test")


class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        #self.bot = webdriver.Chrome("C:\\Users\\Prachi Bindal\\anaconda3\\chromedriver.exe")
        self.bot=driver
        self.login()

    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
        
        #first pop-up 
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)
        
        #2nd pop-up
        self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)
        
        #direct button        
        self.bot.find_element_by_xpath('//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
        time.sleep(3)
        
        #clicks on pencil icon 
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
        time.sleep(2)
        for i in user:
            #enter the username
            self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(2)
            #click on the username
            self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div').click()
            time.sleep(2)
            #next button
            self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(2)
            #click on message area
            send = self.bot.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            #types message
            send.send_keys(self.message)
            time.sleep(1)
            #send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)
            #clicks on direct option or pencl icon
            self.bot.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)

def init():
    bot('abcdemo10', 'abcdemo', user, message_)
    input("DONE")



init()
