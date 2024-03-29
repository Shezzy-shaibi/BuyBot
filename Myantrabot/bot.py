from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from os import path
from bs4 import BeautifulSoup
from configparser import ConfigParser
import random
import time
from selenium.webdriver.support.select import Select
import os
class Bot():
    def __init__(self):
        self.config = self.getConfig()
        self.checkout_url = 'https://www.myntra.com/checkout/cart'

        chrom_options = Options()

        chrom_options.page_load_strategy = 'normal'
        chrom_options.add_argument('--load-extension=/Users/apple/Downloads/BestBuyBot')
        # chrom_options.add_argument("--headless")
        # chrom_options.add_argument("--no-sandbox")
        # chrom_options.add_argument("--disable-dev-shm-usage")
        # chrom_options.add_argument("window-size=1920x1480")


        self.driver = webdriver.Chrome(self.config.get('CHROMEDRIVER_PATH', 'chromdriver_path'), options=chrom_options)
        self.main()


    def main(self):
        # waits for items to load if it hasnt loaded already
        self.driver.implicitly_wait(10)
        # get product page
        self.driver.get(self.config.get('URL', 'item_url'))
        try:
            if self.config.get('SIZE', 'size') == "XS":
                random_wait_time = random.randrange(5.0, 10.0)
                print(random_wait_time)
                time.sleep(random_wait_time)
                self.driver.find_element_by_xpath('//*[@id="sizeButtonsContainer"]/div[2]/div[1]/div[1]/button').click()
            elif self.config.get('SIZE', 'size') == "S":
                random_wait_time = random.randrange(5.0, 10.0)
                print(random_wait_time)
                time.sleep(random_wait_time)
                self.driver.find_element_by_xpath('//*[@id="sizeButtonsContainer"]/div[2]/div[2]/div[1]/button').click()
            elif self.config.get('SIZE', 'size') == "M":
                random_wait_time = random.randrange(5.0, 10.0)
                print(random_wait_time)
                time.sleep(random_wait_time)
                self.driver.find_element_by_xpath('//*[@id="sizeButtonsContainer"]/div[2]/div[3]/div[1]/button').click()
            elif self.config.get('SIZE', 'size') == "L":
                random_wait_time = random.randrange(5.0, 10.0)
                print(random_wait_time)
                time.sleep(random_wait_time)
                self.driver.find_element_by_xpath('//*[@id="sizeButtonsContainer"]/div[2]/div[4]/div[1]/button').click()

            else:
                random_wait_time = random.randrange(5.0, 10.0)
                print(random_wait_time)
                time.sleep(random_wait_time)

                self.driver.find_element_by_xpath('//*[@id="sizeButtonsContainer"]/div[2]/div[5]/div[1]/button').click()
            random_wait_time = random.randrange(5.0, 10.0)
            print(random_wait_time)
            time.sleep(random_wait_time)
            self.driver.find_element_by_class_name('pdp-add-to-bag').click()
        except:
            random_wait_time = random.randrange(5.0, 10.0)
            print(random_wait_time)
            time.sleep(random_wait_time)
            self.driver.find_element_by_class_name('pdp-add-to-bag').click()

        random_wait_time = random.randrange(5.0, 10.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        # redirect to checkout page
        self.driver.get(self.checkout_url)
        if self.config.get('QUANTITY', 'quantity') > "1" and self.config.get('QUANTITY', 'Random') == "False":
            random_wait_time = random.randrange(5.0, 10.0)
            print(random_wait_time)
            time.sleep(random_wait_time)
            self.driver.find_element_by_xpath('//*[@id="cartItemsList"]/div/div/div/div/div[2]/div/div[3]/div/div[2]/span').click()
            for i in range(1,10):
                random_wait_time = random.randrange(5.0, 10.0)
                print(random_wait_time)
                time.sleep(random_wait_time)
                if self.config.get('QUANTITY', 'quantity') == str(i) :
                    self.driver.find_element_by_xpath(f'//*[@id="{i}"]/div').click()
                    break
            self.driver.find_element_by_xpath('//*[@id="cartItemsList"]/div/div/div/div/div[4]/div/div[3]').click()
        elif self.config.get('QUANTITY','Random') == "True":
            random_wait_time=random.randrange(5.0, 10.0)
            time.sleep(random_wait_time)
            random_quantity = random.randrange(1.0, 5.0)
            self.driver.find_element_by_xpath(f'//*[@id="{random_quantit}/div').click()
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="appContent"]/div/div/div/div/div/div[2]/div[3]/a/div').click()
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="reactPageContent"]/div/div/div[2]/div[2]/div[1]/input').send_keys(self.config.get('Personal Information', 'phone_number'))
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="reactPageContent"]/div/div/div[2]/div[2]/div[3]').click()
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="reactPageContent"]/div/div[3]').click()
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="reactPageContent"]/div/div/form/div/div[2]/input').send_keys(self.config.get('Personal Information', 'password'))
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="reactPageContent"]/div/div/form/div/div[3]/button').click()
        """
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="cartItemsList"]/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/span').click()
        random_wait_time = random.randrange(5.0, 15.0)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="cartItemsList"]/div/div/div/div/div[2]/div/div[3]/div[1]/div[2]/span').click()
        """
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        self.driver.find_element_by_xpath('//*[@id="appContent"]/div/div/div/div/div/div[2]/div[3]/a/div').click()
        random_wait_time = random.randrange(5.0, 15.0)
        print(random_wait_time)
        time.sleep(random_wait_time)
        # fill in email and phone number
        # fill in email and phone number
        try:
            self.personalInformation()



            self.billingAddressPayment()

            random_wait_time = random.randrange(5.0, 11.0)
            print(random_wait_time)
            time.sleep(random_wait_time)
            self.driver.find_element_by_class_name('//*[@id="appContent"]/div/div/div/div/div[1]/div/div/div[2]/div').click()
            random_wait_time = random.randrange(5.0, 15.0)
            print(random_wait_time)
            time.sleep(random_wait_time)
            self.driver.find_element_by_xpath('//*[@id="placeOrderButton"]').click()

        except NoSuchElementException:
            print("YES")
            random_wait_time = random.randrange(5.0, 15.0)
            print(random_wait_time)
            time.sleep(random_wait_time)
            self.driver.find_element_by_xpath('//*[@id="placeOrderButton"]').click()
            random_wait_time = random.randrange(5.0, 15.0)
            print(random_wait_time)
            time.sleep(random_wait_time)

        if self.config.get('Check', 'credit_card') == "True":
            # Credit Card
            self.driver.find_element_by_xpath('//*[@id="card"]/span/span/div[2]/span').click()
            # enter in credit card information
            self.creditCard()

        else:
            # Cash on delivery
            self.driver.find_element_by_xpath('//*[@id="action-cod"]').click()




        # pay
        self.driver.find_element_by_xpath('//*[@id="action-card"]').click()

        self.driver.find_element_by_xpath('//*[@id="payuMcpForm"]/div[2]/div/p/button').click()


    def getConfig(self):
        config = ConfigParser()
        if path.exists('config.mine.ini'):
            config.read('config.mine.ini')
        else:
            config.read('config.ini')
        return config


    def goToCheckout(self):
        self.driver.find_element_by_class_name('btn-primary').click()
        self.driver.find_element_by_class_name('guest').click()


    def personalInformation(self):
        name = self.driver.find_element_by_xpath('//*[@id="name"]')
        phone_number_field = self.driver.find_element_by_xpath('//*[@id="mobile"]')

        name.send_keys(self.config.get('Personal Information', 'name'))
        phone_number_field.send_keys(self.config.get('Personal Information', 'phone_number'))


    def billingAddressPayment(self):
        # first_name_field = self.driver.find_element_by_id('payment.billingAddress.firstName')
        # last_name_field = self.driver.find_element_by_id('payment.billingAddress.lastName')
        zip_code_field = self.driver.find_element_by_xpath('//*[@id="pincode"]')
        address_field = self.driver.find_element_by_xpath('//*[@id="streetAddress"]')
        town = self.driver.find_element_by_xpath('//*[@id="locality"]')
        landmark = self.driver.find_element_by_xpath('//*[@id="landmark"]')
        #city_field = self.driver.find_element_by_id('payment.billingAddress.city')
        #state_field = Select(self.driver.find_element_by_id('payment.billingAddress.state'))

        #first_name_field.send_keys(self.config.get('Billing Address', 'first_name'))
        #last_name_field.send_keys(self.config.get('Billing Address', 'last_name'))
        zip_code_field.send_keys(self.config.get('Billing Address', 'zip_code'))
        address_field.send_keys(self.config.get('Billing Address', 'address'))
        town.send_keys(self.config.get('Billing Address', 'town'))
        landmark.send_keys(self.config.get('Billing Address', 'landmark'))
        # city_field.send_keys(self.config.get('Billing Address', 'city'))
        # state_field.select_by_visible_text(self.config.get('Billing Address', 'state'))
        # zip_code_field.send_keys(self.config.get('Billing Address', 'zip_code'))


    def billingAddressConsolidated(self):
        # consolidated sometimes changes; consolidatedAddresses.ui_address_xxxx.lastName
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        div = soup.find('div', {'class' : 'form-group'})
        consolidated_template = div.input['id'].replace('firstName', '')

        first_name_field = self.driver.find_element_by_id(consolidated_template + 'firstName')
        last_name_field = self.driver.find_element_by_id(consolidated_template + 'lastName')
        address_field = self.driver.find_element_by_id(consolidated_template + 'street')
        city_field = self.driver.find_element_by_id(consolidated_template + 'city')
        state_field = Select(self.driver.find_element_by_id(consolidated_template + 'state'))
        zip_code_field = self.driver.find_element_by_id(consolidated_template + 'zipcode')

        first_name_field.send_keys(self.config.get('Billing Address', 'first_name'))
        last_name_field.send_keys(self.config.get('Billing Address', 'last_name'))
        address_field.send_keys(self.config.get('Billing Address', 'address'))
        city_field.send_keys(self.config.get('Billing Address', 'city'))
        state_field.select_by_visible_text(self.config.get('Billing Address', 'state'))
        zip_code_field.send_keys(self.config.get('Billing Address', 'zip_code'))


    def creditCard(self):
        #send card number first and then rest will show up
        card_number_field = self.driver.find_element_by_xpath('//*[@id="cardNumber"]')
        card_number_field.send_keys(self.config.get('Credit Card', 'card_number'))

        name_on_card = self.driver.find_element_by_xpath('//*[@id="cardName"]')
        name_on_card.send_keys(self.config.get('Credit Card', 'name_on_card'))

        expiration_month_field = self.driver.find_element_by_xpath('//*[@id="expiry"]')
        month = self.config.get('Credit Card', 'expiration_month')
        year = self.config.get('Credit Card', 'expiration_year')
        month_year = f'{month}{year}'
        expiration_month_field.send_keys(month_year)

        security_code_field = self.driver.find_element_by_xpath('//*[@id="cvv"]')
        security_code_field.send_keys(self.config.get('Credit Card', 'security_code'))


if __name__ == '__main__':
    bot = Bot()
