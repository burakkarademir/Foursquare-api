from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from rauth import OAuth2Service
import requests
import json

foursquare = OAuth2Service(
    client_id="4MFAWW1AEBFUIEROU42D0YOCRSXFMKETV3LVVVJ2JY4U3CXK",
    client_secret="GZAIUSEJF1DJS31DEWGA2WI21PEENCA0UDV0NC1FCZTUMRGO",
    name='foursquare',
    authorize_url='https://foursquare.com/oauth2/authenticate',
    access_token_url='https://foursquare.com/oauth2/access_token',
    base_url='https://api.foursquare.com/v2/')

redirect_uri = 'http://localhost'

params = {'response_type': 'token',
          'redirect_uri': redirect_uri}

authorize_url = foursquare.get_authorize_url(**params)

#-----------LOGIN INSTAGRAM----------------#

#starting a new browser session
browser=webdriver.Chrome('C:\webdrivers\chromedriver.exe')

#navigating to a webpage
browser.get('https://tr.foursquare.com/login')

userId=input("email:")
password= input("password: ")
#find form inputs and enter data
inputs=browser.find_elements_by_xpath('//form/p/input')

ActionChains(browser)\
    .move_to_element(inputs[0])\
    .click().send_keys(userId)\
    .move_to_element(inputs[1]).click()\
    .send_keys(password)\
    .perform()

#find Log in button and click it
login_button = browser.find_element_by_xpath('//form/p/button')

ActionChains(browser)\
    .move_to_element(login_button)\
        .click().perform()

url = 'https://api.foursquare.com/v2/users/{}?oauth_token=AFM1CVKS0W1K3MG2CQK5HOLGNMXP4ZPYQNWE253HGKIKBXYW&v=20190809'

userId= input("user id:")




resp = requests.get(url=url.format(userId))
data = json.loads(resp.text)
print(json.dumps(data,indent = 4))

#make sure the browser stays open for 5sec
sleep(30)

#clean exit
browser.close()