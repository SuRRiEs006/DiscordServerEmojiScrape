# DiscordServerEmojiScrape / EmojiDetailScrape

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import win32clipboard
from selenium.webdriver.common.keys import Keys
import requests
""" HAVE TO MANUALLY TAKE THE SCRIPT TO THE EMOJI PAGE FOR SCRAPE """

def clip2pad(FName, copyin=True):
    if copyin == True:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        print data
        with open(str(FName)+".txt", "a") as myfile:
            myfile.write(data+"\n")
    elif copyin != True:
        with open(str(FName)+".txt", "a") as myfile:
            myfile.write(copyin+"\n")
            
def emojiScrape(browser,EmojNum):
    for i in range(2,(EmojNum+2)):
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/main/div[1]/div[2]/div[1]/div["+str(i)+"]/div[2]/div[1]/input").send_keys(Keys.CONTROL, 'a')
        time.sleep(0.1)
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/main/div[1]/div[2]/div[1]/div["+str(i)+"]/div[2]/div[1]/input").send_keys(Keys.CONTROL, 'c')
        clip2pad("EmojiName")
###############################################################
    for j in range(2,(EmojNum+2)):
        EmojimgURL = browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/main/div/div[2]/div[1]/div["+str(j)+"]/div[1]").get_attribute("style")
        finalEmojiURL = EmojimgURL[23:79]
        clip2pad("EmojiImageURL",finalEmojiURL)
        
        
def readyup(username,password):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1000,831")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    time.sleep(0.5)
    browser.get("https://discord.com/channels/@me")
    time.sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input").click()
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input").send_keys(username)
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input").click()
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input").send_keys(password)
    time.sleep(15)
    return(browser)
    
browser = readyup("REPLACE WITH EMAIL","REPLACE WITH PASSWORD")
emojiScrape(browser,40)
