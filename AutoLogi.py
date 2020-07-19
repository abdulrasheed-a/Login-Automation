from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("---+ AutoLogi +---")
print("******************")
path="enter the driver path here"
print(" 1.Facebook 2.Twitter \n 2.Help")
n=int(input("Choose an option: "))
if(n==1):
    print("AutoLogi is loading ...Please wait...")
    username='your_fb_username'
    password='your_fb_pass'
    url='https://www.facebook.com/'
    driver=webdriver.Chrome(path)
    driver.get(url)
    driver.find_element_by_id("email").send_keys(username);
    driver.find_element_by_id("pass").send_keys(password,Keys.RETURN); 
   # driver.find_element_by_id("u_0_b").click();
elif(n==2):
    print("AutoLogi is loading ...Please wait...")
    username='your_twitter_username'
    password='your_twitter_pass'
    url='https://twitter.com/login'
    driver=webdriver.Chrome(path)
    driver.get(url)
    driver.find_element_by_name("session[username_or_email]").send_keys(username)
    driver.find_element_by_name("session[password]").send_keys(password,Keys.RETURN)
else:
    print("Need Help?")
    print("Here are some solutions\n")
    print("->Make sure you have downloaded the appropriate driver of your browser and put it in the given driver path\n")
    print("->Websites may have changed the ids of the login box, then change it in the program and please report us")