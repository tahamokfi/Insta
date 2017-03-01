import os
from selenium import webdriver
import sys
import bs4
import time
import time
import random
import selenium
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
def Instfolme():
    user1 = input("Please enter your UserName: ")
    pass1 = input("Please enter your Password: ")
    id1 = input("Please enter your Instagram ID (might be same as UserName):")
    #start driver
    driver=webdriver.PhantomJS()
    print("\n","\n","Please wait while loading your freinds list")
    driver.set_window_size(1120, 550)
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    #Username
    elm1=driver.find_element_by_name("username")
    elm1.click()
    elm1.send_keys(user1)
    #Password
    elm2=driver.find_element_by_name("password")
    elm2.click()
    elm2.send_keys(pass1)
    #Click on login
    elm4=driver.find_element_by_xpath("//span[1]/button")
    elm4.click()
    time.sleep(5)
    #Error
    try:
        #Navigate to profile and followers
        driver.get("https://www.instagram.com/"+id1)
        elm4=driver.find_element_by_xpath("//div[2]/ul/li[2]/a")
        elm4.click()
        time.sleep(2)
    except NoSuchElementException:
        sys.exit("Username or Password are incorrect")
    #find the followers window
    dialog = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
    #find number of followers
    allfoll=int(driver.find_element_by_xpath("//li[2]/a/span").text) 
    #scroll down the page
    for i in range(int(allfoll/2)):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
        time.sleep(random.randint(500,1000)/1000)
        print("Extract friends %",round((i/(allfoll/2)*100),2),"from","%100")
    #get followers name and status
    pg1=driver.page_source
    elm1=bs4.BeautifulSoup(pg1,"lxml")
    tm1=elm1.find_all("a",{"class":"_4zhc5 notranslate _j7lfh"})
    tm2=elm1.find_all("span",{"class":"_7k49n _hvnxx"})
    #extrct text from followers and status link
    nm1=[]
    st1=[]
    for i in tm1:
        nm1.append(i.text)
    for i in tm2:
        st1.append(i.text)
    st1.pop(0)
    #list of followers that you have followed
    return([nm1[i] for i in [i for i, x in enumerate(st1) if x == "Following"]])
fol1=Instfolme()
fol2=pd.DataFrame([fol1]).T
fol2.to_csv(os.path.expanduser('~')+"\\Insta101.csv",index=False)
print("\n","\n","The CSV containing your friends is been saved here",os.path.expanduser('~')+"\\Insta101.csv")
print("This list would be the list of your friends that you are following them")