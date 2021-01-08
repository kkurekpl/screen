from selenium import webdriver
from time import sleep
from PIL import Image
browser = webdriver.Chrome()
browser.get('onet.pl')
sleep(1)
featureElement = browser.find_element_by_xpath('//section[contains(string(),’START SCREENSHOT TESTING’)]')
location = featureElement .location
size = featureElement .size
browser.save_screenshot('fullPageScreenshot.png')
x = location[x]
y = location[y]
w = x + size[width]
h = y + size[height]
fullImg = Image.open('fullPageScreenshot.png')
cropImg = fullImg.crop(x, y, w, h)
cropImg.save(cropImage.png)
browser.quit()