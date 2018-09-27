from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time




def main(usr,psw,reponme,repodsc):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_driver = os.getcwd() +"\\chromedriver.exe"

    browser=webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    browser.get("https://github.com/login") 

    username=browser.find_element_by_xpath("//*[@id='login_field']")
    pw=browser.find_element_by_xpath("//*[@id='password']")

    username.send_keys(usr) 
    pw.send_keys(psw) 

    login=browser.find_element_by_xpath("//*[@id='login']/form/div[3]/input[3]")
    login.click()
    time.sleep(1)

    print ("Giriş yapıldı.")

    browser.get("https://github.com/new")
    time.sleep(1)
    reponame=browser.find_element_by_xpath("//*[@id='repository_name']")
    repodesc=browser.find_element_by_xpath("//*[@id='repository_description']")
    submitrepo=browser.find_element_by_xpath("//*[@id='new_repository']/div[3]/button")

    print ("Pathler alındı.")

    reponame.send_keys(reponme)
    time.sleep(1)
    repodesc.send_keys(repodsc)
    time.sleep(1)
    submitrepo.click()

    print ("İşlem başarılı.")

    repolink=browser.find_element_by_xpath("//*[@id='empty-setup-clone-url']")
    print ("Link oluşturuldu.")
    print(repolink.get_attribute('value'))

usr="" # username
psw=""  # password
print("----------------")
reponm=input("Repository name: ")
repodsc=input("Repo description: ")

print("İşlem başladı..")

main(usr,psw,reponm,repodsc)
    