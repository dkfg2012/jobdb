from selenium import webdriver
import csv
from time import sleep

chromedriver = "C:/Users/WingHo/Desktop/programming/jobdb/chromedriver"
driver = webdriver.Chrome(chromedriver)

'''login part'''
driver.get("https://hk.jobsdb.com/hk/en/login/jobseekerlogin?from=header")
email = ''  #enter email address
password = ''   #enter password

email_input = driver.find_element_by_xpath('//input[@name="c_JbSrP1LnItDap_El0"]')
password_input = driver.find_element_by_xpath('//input[@name="c_JbSrP1LnItDap_Pd0"]')

email_input.send_keys(email)
password_input.send_keys(password)

driver.find_element_by_xpath('//button[@id="reg-login-button"]').click()

'''job application part'''
with open('jobSearch.csv', newline='') as f:
    rows = csv.reader(f)
    for row in rows:
        print(row[0])
        sleep(10) #to ensure the driver have enoggh time to load the page
        driver.get(row[0])
        try:
            #since some job opening have been closed when I write this function, so using try 
            apply_link = driver.find_element_by_xpath('//a[@class="_37Yu17M _3laJqVT _16YdUsX _2nPU7y8"]').get_attribute("href")
            print(apply_link)
            driver.get(apply_link)
            driver.find_element_by_xpath('//button[@name="BtnProfileApply"]').click()
        except:
            pass

        with open('result.csv', 'a') as r:
            r.write(row[0] + '\n') #to collect which company have just applied, so I wont apply it next time.



