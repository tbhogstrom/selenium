from selenium import webdriver
from Pillow import Image

def takepic(url)
	fp = webdriver.FirefoxProfile('C:/Users\Tyler Hogstrom/AppData/Roaming/Mozilla/Firefox/Profiles/fyhue1vr.default')
	browser = webdriver.Firefox(fp)
	browser.get(url)
	pic = browser.save_screenshot('screenie.png')
	im = Image.open(pic)
	print(im.format, im.size, im.mode)
	browser.quit()