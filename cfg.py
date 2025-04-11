from selenium.webdriver.common.by import By

URL_LOGIN = "https://www.saucedemo.com"
URL_PRODUCT = "https://www.saucedemo.com/inventory.html"
URL_CART = "https://www.saucedemo.com/cart.html"
URL_CHECKOUT = "https://www.saucedemo.com/checkout-step-one.html"
URL_OVERVIEW = "https://www.saucedemo.com/checkout-step-two.html"
URL_FINISH = "https://www.saucedemo.com/checkout-complete.html"

USERNAME = "standard_user" 
PASSWORD = "secret_sauce" 

TEST_REMOVE = (By.CSS_SELECTOR,"button[class='btn btn_secondary btn_small btn_inventory ']")
SORT_METHODS = ['Name (A to Z)' , 'Name (Z to A)' , 'Price (low to high)', 'Price (high to low)']


NAME_AZ = 'Name (A to Z)'
NAME_ZA = 'Name (Z to A)'
PRICE_UP = 'Price (low to high)'
PRICE_DOWN = 'Price (high to low)'

BIGTEXT = "Thank you for your order!"
MINTEXT = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"