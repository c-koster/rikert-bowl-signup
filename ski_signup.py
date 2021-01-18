"""
A little selenium script to register me at rikert or the snowbowl. I useed xpath
and id locators to navigate through the reservation page.

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import datetime

today = str(datetime.datetime.today()).split()[0]

rikert_link = "https://rikertnordiccenter.ltibooking.com/purchase-path/product-details/13207?date=" + today


driver = webdriver.Chrome(executable_path='/users/cultonkoster/Desktop/found-on-desktop/chromedriver')

def rikert_signup(firstname,lastname,email,passholder_id,date=today):

    # go to the web addresss for today's date (or other if specified)
    driver.get(rikert_link)

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

    print(f"Submitted a reservation for {lastname},{firstname} on {today}")


# for if you're using this as a command line tool
if __name__ == "__main__":

    import sys
    if len(sys.argv) == 5:
        rikert_signup(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

    elif len(sys.argv) == 5:
        rikert_signup(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],date=sys.argv[5])

    else:
        print(f"usage: python3 {sys.argv[0]} <first> <last> <email> <id> (YYYY-MM-DD)")
