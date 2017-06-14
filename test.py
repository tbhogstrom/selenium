from selenium import webdriver
#extent.config().addCustomStylesheet("C:\\css.css");
fp = webdriver.FirefoxProfile('C:/Users\Tyler Hogstrom/AppData/Roaming/Mozilla/Firefox/Profiles/fyhue1vr.default')
browser = webdriver.Firefox(fp)
# custom styles
#style =".m-leaderboard{background-color:#000 !important;color:#ff0000 !important;}";
#browser.config().addCustomStyles(style);
browser.get('http://www.digitaltrends.com/')
browser.save_screenshot('screenie.png')
browser.quit()