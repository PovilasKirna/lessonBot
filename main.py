import json
import time
import random
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
    
def initiateDriver():
  opt = Options()
  opt.add_argument("--disable-infobars")
  opt.add_argument("start-maximized")
  opt.add_argument("--disable-extensions")
  # Pass the argument 1 to allow and 2 to block
  opt.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_mic": 1, 
      "profile.default_content_setting_values.media_stream_camera": 1,
      "profile.default_content_setting_values.geolocation": 1, 
      "profile.default_content_setting_values.notifications": 1 
    })

  return webdriver.Chrome("/Users/Povilas/Documents/GitHub/chromedriver", options=opt)
  
    
def joinLesson(driver, lessonName):
  lesson_url = ""
  lesson_code = ""
  with open('lessons.json') as file:
      data = json.load(file)
      for lesson in data["lessons"]:
          if lesson["Name"] == lessonName:
              lesson_url = lesson["URL"]
              lesson_code = lesson["Code"]
              
              
  driver.get(lesson_url)
  time.sleep((random.randint(30,50))/10)
  driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div[2]/div/div/span").click()
  time.sleep((random.randint(30,50))/10)
  driver.find_element_by_xpath("/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a").click()
  time.sleep((random.randint(30,50))/10)
  emailinput = driver.find_element_by_css_selector("input[type='email']")
  emailinput.click()
  emailinput.send_keys(os.getenv("schoolMail"))#Your email to join google meets
  time.sleep((random.randint(5,20))/10)
  emailinput.send_keys(Keys.RETURN)
  time.sleep((random.randint(30,50))/10)
  passinput = driver.find_element_by_css_selector("input[type='password']")
  passinput.click()
  passinput.send_keys(os.getenv("schoolMailPassword"))#Your password to join google meets
  time.sleep((random.randint(5,20))/10)
  passinput.send_keys(Keys.RETURN)
  time.sleep((random.randint(30,50))/10)
  driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]").click()
  time.sleep((random.randint(30,50))/10)
  codeinput= driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input")
  codeinput.click()
  codeinput.send_keys(lesson_code)
  time.sleep((random.randint(30,50))/10)
  driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span").click()
  time.sleep((random.randint(50,70))/10)
  driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div/span/span/div/div[1]/div").click()
  time.sleep((random.randint(10,50))/10)
  driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div").click()
  time.sleep((random.randint(30,50))/10)
  driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span").click()
  time.sleep((random.randint(30,50))/10)
  print("Successfuly joined the lesson!")
  
  
def main():
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  while current_time != "16:00:00":
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    time.sleep(1)
    if current_time == "09:00:00":#-------------- time when to join the lesson
      driver = initiateDriver()
      joinLesson(driver, "Mathematics")
  
if __name__ == "__main__":
  load_dotenv()
  main()
  quit()
