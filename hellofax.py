from selenium import webdriver
from twilio import TwilioRestClient
from twilio import TwilioRestException
from selenium.webdriver.common.keys import Keys

print("Python hellofax script running.......")
print("Loading website(hellofax.com).....................")
browser=webdriver.Chrome('/home/dinesh10c04/Desktop/Pro/chromedriver')
browser.get("https://www.hellofax.com")
browser.find_element_by_id('signinButton').click()
print("Sign in page opened")
browser.find_element_by_id('login_email_address').send_keys('dineshfax@gmail.com')
print("Email input success")
browser.find_element_by_id('login_password').send_keys('3158233dinesh')
print("Password input success")
print("Loggin in ........")
browser.find_element_by_id('login').click()
print("Uploading the fax.......")
browser.find_element_by_name('file').send_keys('/home/dinesh10c04/Desktop/fax')
print("Fax uploaded....")
browser.find_element_by_xpath('//input[@class="recipient ui-autocomplete-input"]').send_keys('04424500050')
print("Hostel fax number input sucess....")
browser.find_element_by_xpath('//div[@style="z-index: 998;"]').click()
browser.find_element_by_xpath('//span[@class="destination multiple_destinations"]').click()
browser.find_element_by_xpath('//div[@country="India"]').click()
print("India destination selection sucess")
browser.find_element_by_id('tsm_group_send_submit')
print("Send element found")

try:
    print("Sending SMS Twilio")
    twilioclient=TwilioRestClient("AC76e91031d6f3413bd4601804cfb2e331","933548b0af97f39b9b38624b357f0ea6")
    messsages=twilioclient.messages.create(to="+919843789901",from_="+919843789901",body="Send operation sucess.. The site is now sendind the fax... Please wait")
except TwilioRestClient as e:
    print(e)
