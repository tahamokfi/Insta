import os
from selenium import webdriver
import sys
import bs4
import time
import random
import selenium
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
tm3,nm3,nm4,pr2,pr3=[],[],[],[],[]
k=1
def instfol(lis1,frnd=100,frnd1=3):
    print('Make sure that this file '+os.path.expanduser('~')+"\\Insta101.csv"+" exists (You can create this file using Instfolme function)")
    user1 = input("Please enter your UserName: ")
    pass1 = input("Please enter your Password: ")
    id1 = input("Please enter your Instagram ID (might be same as UserName):")
    #start driver
    driver=webdriver.Chrome()
    print("\n","\n","Please wait!")
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
    for i in range(frnd1):
        ln1=str("https://www.instagram.com/"+str(lis1[i])+"/")
        driver.get(ln1)
        nnm1=str(lis1[i])
        time.sleep(3)
        #Navigate to followers
        elm4=driver.find_element_by_xpath("//div[2]/ul/li[2]")
        elm4.click()
        #find the followers window
        time.sleep(1)
        dialog = driver.find_elements_by_class_name('_4gt3b')[0]
        time.sleep(1)
        #find number of followers
        allfoll=int(driver.find_element_by_xpath("//li[2]/a/span").text.replace(",",""))
        if allfoll>frnd:
            rng1=frnd
        else:
            rng1=allfoll
        #scroll down the page
        for j in range(int(frnd)):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            #time.sleep(random.randint(200,400)/1000)
            pg1=driver.page_source
            elm1=bs4.BeautifulSoup(pg1,"lxml")
            tm3=len(elm1.find_all("a",{"class":"_4zhc5 notranslate _j7lfh"}))
            if tm3+1>=rng1:
                break
        pg1=driver.page_source
        elm1=bs4.BeautifulSoup(pg1,"lxml")
        tm3=elm1.find_all("a",{"class":"_4zhc5 notranslate _j7lfh"})
        nm2=[]
        for i in tm3:
            nm2.append(i.text)
        pr1=[]
        import itertools
        pr1=list(itertools.repeat(nnm1, len(nm2)))
        pr2.append(pr1)
        nm3.append(nm2)
        time.sleep(random.randint(500,1500)/1000)
        print("Now extrcating "+nnm1+" Followers") 
    return(pr2,nm3)
fol1=pd.read_csv(os.path.expanduser('~')+"\\Insta101.csv")
fol1=fol1['0'].tolist()
frnd = input("How many followers from each person do you want to have?  ")
frnd1 = input("How many of your freinds do you want to search for?  ")
fo1=instfol(fol1,int(frnd),int(frnd1))
nm1=[val for sublist in fo1[0] for val in sublist]
nm2=[val for sublist in fo1[1] for val in sublist]
fol3=pd.DataFrame([nm1,nm2]).T
fol3.to_csv(os.path.expanduser('~')+"\\Follist101.csv",index=False)
fol3.columns=["From","To"]
print("\n","\n","The CSV containing your friends and their followers is been saved here",os.path.expanduser('~')+"\\Insta101.csv")