from selenium import webdriver
from PIL import Image
import io
import numpy as np

def takepic(url):
	fp = webdriver.FirefoxProfile('C:/Users\Tyler Hogstrom/AppData/Roaming/Mozilla/Firefox/Profiles/fyhue1vr.default')
	browser = webdriver.Firefox(fp)
	browser.set_window_size(1280,800)
	browser.get(url)
	bytepic = browser.get_screenshot_as_png()
	browser.quit()
	pic = io.BytesIO(bytepic)
	return(pic)

def analysepic(pic):
	adpix = 0
	nonadpix = 0
	im = Image.open(pic)
	for pixel in im.getdata():
		if pixel == (255 , 0 , 0, 255):
			adpix += 1
		else:
			nonadpix += 1
	ratio = (adpix/(nonadpix + adpix))*100
	print('the ratio of ad pixels on pageload is '+ str(ratio)+'%.')