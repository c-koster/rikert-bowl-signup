"""
A little selenium script to register me at rikert or the snowbowl. I useed xpath
and id locators to navigate through the reservation page.

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import os
import datetime

today = str(datetime.datetime.today()).split()[0]


# setup if running on heroku -- implies there is an environment variable called 'LOCAL'
chrome_options = webdriver.ChromeOptions()

if os.environ.get("LOCAL"):

    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def rikert_signup(firstname,lastname,email,passholder_id,date=today):
    rikert_link = "https://rikertnordiccenter.ltibooking.com/purchase-path/product-details/13207?date=" + today
    return ski_signup(firstname,lastname,email,passholder_id,rikert_link)

def bowl_signup(firstname,lastname,email,passholder_id,date=today):

    bowl_link = "https://middleburysnowbowl.ltibooking.com/purchase-path/product-details/13198?date=" + today
    return ski_signup(firstname,lastname,email,passholder_id,bowl_link)


def ski_signup(firstname,lastname,email,passholder_id,link):
    # ok they use the exact same system it just matters which page you start at..
    # go to the web addresss for today's date (or other if specified)
    try:
        driver.get(link)

        # find (by text) and click continue button
        cont_button = driver.find_element_by_xpath("//*[text()[contains(., 'Continue')]]")
        cont_button.click()

        # enter first name, last name, and email
        first_box = driver.find_element_by_id("v1_user_account_first_name")
        first_box.send_keys(firstname)

        last_box = driver.find_element_by_id("v1_user_account_last_name")
        last_box.send_keys(lastname)

        email_box = driver.find_element_by_id("v1_user_account_email")
        email_box.send_keys(email)


        save_button = driver.find_element_by_xpath("//*[text()[contains(., 'Save Your Information')]]")
        save_button.click()

        # same for passholder info
        first_box = driver.find_element_by_id("v1_purchase_order_line_items_attributes_0_first_name")
        first_box.send_keys(firstname)

        last_box = driver.find_element_by_id("v1_purchase_order_line_items_attributes_0_last_name")
        last_box.send_keys(lastname)

        res_box = driver.find_element_by_id("v1_purchase_order_line_items_attributes_0_custom_value_1")
        res_box.send_keys(passholder_id)

        save_button = driver.find_element_by_xpath("//*[text()[contains(., 'Save Passholder Information')]]")
        save_button.click()

        # last page push send!
        submit_button = driver.find_element_by_xpath("//*[text()[contains(., 'Submit Order')]]")
        submit_button.click()
        #print(f"Submitted a reservation for {lastname},{firstname} on {today}")

        return True
    except:
        return False

# if you're using this as a command line tool
if __name__ == "__main__":

    import sys
    if len(sys.argv) == 5:
        rikert_signup(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

    elif len(sys.argv) == 6:
        rikert_signup(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],date=sys.argv[5])

    else:
        print(f"usage: python3 {sys.argv[0]} <first> <last> <email> <id> (YYYY-MM-DD)")
