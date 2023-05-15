import time
from selenium import webdriver
from selenium.webdriver.chrome import service

from selenium.webdriver.common.by import By

webdriver_service = service.Service("D:/Apps/operadriver_win64/operadriver_win64/operadriver.exe")
webdriver_service.start()

options = webdriver.ChromeOptions()
options.binary_location = "C:/Users/username/AppData/Local/Programs/Opera GX/opera.exe"
options.add_argument('--user-data-dir=D:/Apps/OperaCopySelenium/Opera GX Stable')
options.add_experimental_option('w3c', True)

driver = webdriver.Remote(webdriver_service.service_url, options=options)
time.sleep(5)  # see the result

# ----------------------------------------------------------

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="#cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID,value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID,value="cps").text
        print(cookie_per_s)
        break

driver.quit()