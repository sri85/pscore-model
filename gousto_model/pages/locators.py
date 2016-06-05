from selenium.webdriver.common.by import By


class Locators(object):
    GOUSTO_HEADER = By.XPATH, '//*[@id="navrow"]'
    GOUSTO_FOOTER = By.XPATH, '//*[@id="footer-strip"]'
    DELIVERY_DATE = By.XPATH, '//*[@id="delivery-day-btns"]/div[1]/div/a[2]'
    SELECT_DELIVERY_DATE = By.XPATH, '//*[@id="delivery-day-btns"]/div[1]/div/a[2]'
    ADD_BUTTON = By.CSS_SELECTOR, 'farm-shop .notinbasket .addtobasket.plus, body.this-weeks-recipes .notinbasket .addtobasket.plus'
    ADDED_BUTTON = By.CSS_SELECTOR, '#farm-shop .addedtobasket, body.this-weeks-recipes .addedtobasket'
    REMOVE_BUTTON = By.CSS_SELECTOR, '#ordersummary-box > div > ul > li:nth-child(10) > a'
    MAIN_RECIPE = By.XPATH, '//*[@id="recipe-id-413"]/div/a/span[1]/div'
    BUTTON_CLOSE = By.XPATH, '//*[@id="recipe-show-modal"]/div/div[1]/button'
    RECIPE_INFO = By.XPATH, '//*[@id="show-recipe-target"]/div[2]/div[3]'
    CHECKOUT_BUTTON = By.XPATH, '//*[@id="ordersummary-box-price"]/div/button'
    PORTION_TOGGLE_BUTTON = By.XPATH, '//*[@id="ordersummary-box"]/div/div[2]/a[2]'
    PORTION_TEXT = By.XPATH, '//*[@id="ordersummary-box"]/div/div[5]/p[1]'
    ADD_MORE_RECIPES = By.CSS_SELECTOR, '#ordersummary-box > div > ul > li:nth-child(10) > div > p:nth-child(2) > a'
    ERROR_ALERT = By.XPATH, '//*[@id="alertify-logs"]'
