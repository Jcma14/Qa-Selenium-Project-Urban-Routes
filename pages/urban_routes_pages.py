from data import data
from utilities.retrieve_code import retrieve_phone_code
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_fare = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_number_button = (By.CSS_SELECTOR, '.np-button')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.CSS_SELECTOR, '.button.full')
    sms_code = (By.ID, 'code')
    sms_confirmation_button = (By.XPATH, "//div[@class='buttons']/button[text()='Confirm']")
    phone_number_display_text = (By.CLASS_NAME, 'np-text')
    payment_method_button = (By.CSS_SELECTOR, '.pp-button')
    add_card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.NAME, 'code')
    add_card_submit_button = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Add']")
    new_card_added = (By.CLASS_NAME, 'pp-title')
    payment_method_close_button = (By.XPATH,
                                   '//div[@class="payment-picker open"]'''
                                   '//button[@class="close-button section-close"]'
                                   )
    comment_for_driver_field = (By.ID, 'comment')
    order_requirements_button = (By.CLASS_NAME, 'reqs-header')
    blanket_and_handkerchiefs_slider = (By.XPATH,
                                        "//div[contains(text(), 'Blanket and handkerchiefs')]"
                                        "//ancestor::div[@class='r-sw-container']"
                                        "//span[@class='slider round']"
                                        )
    blanket_and_handkerchiefs_input = (By.XPATH,
                                       "//div[contains(text(), 'Blanket and handkerchiefs')]"
                                       "//ancestor::div[@class='r-sw-container']"
                                       "//input[@class='switch-input']")
    ice_cream_counter_plus_button = (By.XPATH,
                                       "//div[contains(text(), 'Ice cream')]"
                                       "//ancestor::div[@class='r-counter-container']"
                                       "//div[@class='counter-plus']")
    ice_cream_counter_plus_value = (By.XPATH,
                                       "//div[contains(text(), 'Ice cream')]"
                                       "//ancestor::div[@class='r-counter-container']"
                                       "//div[@class='counter-value']")
    book_taxi_button = (By.CLASS_NAME, 'smart-button-main')
    car_search_timer = (By.CLASS_NAME, 'order-header-time')
    driver_details = (By.CLASS_NAME, 'order-btn-rating')



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_call_taxi_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.call_taxi_button)
        )

    def click_on_call_taxi_button(self):
        self.get_call_taxi_button().click()

    def get_comfort_fare(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.comfort_fare)
        )

    def click_on_comfort_fare(self):
        self.get_comfort_fare().click()

    def get_phone_number_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_number_field)
        )
    def set_phone_number_field(self, phone_number):
        self.get_phone_number_field().send_keys(phone_number)

    def get_next_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.next_button)
        )

    def click_on_next_button(self):
        self.get_next_button().click()

    def get_sms_code(self):
        return self.wait.until(
            EC.presence_of_element_located(self.sms_code)
        )
    def set_sms_code(self):
        self.get_sms_code().send_keys(retrieve_phone_code(self.driver))

    def get_sms_confirmation_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.sms_confirmation_button)
        )

    def click_on_confirmation_button(self):
        self.get_sms_confirmation_button().click()

    def get_phone_number_after_confirmation(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_number_display_text)).text

    def get_payment_method_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.payment_method_button)
        )

    def click_on_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.add_card_button)
        )

    def click_on_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        )

    def set_card_number_field(self):
        card_number_field = self.get_card_number_field()
        card_number_field.send_keys(data.card_number)

    def get_card_code_field(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.card_code_field)
        )

    def set_card_code_field(self):
        code_field = self.get_card_code_field()
        code_field.send_keys(data.card_code)
        code_field.send_keys(Keys.TAB)

    def get_add_card_submit_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_card_submit_button)
        )

    def click_on_add_card_submit_button(self):
        self.get_add_card_submit_button().click()

    def get_new_card_added(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.new_card_added)
        )

    def get_payment_method_close_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.payment_method_close_button)
        )

    def click_on_payment_method_close_button(self):
        self.get_payment_method_close_button().click()

    def get_comment_for_driver_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.comment_for_driver_field)
        )

    def set_comment_for_driver_field(self):
        comment_field = self.get_comment_for_driver_field()
        comment_field.send_keys(data.message_for_driver)

    def get_comment_for_driver_value(self):
        return self.get_comment_for_driver_field().get_attribute('value')

    def get_order_requirements_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.order_requirements_button)
        )

    def get_blanket_and_handkerchiefs_slider(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.blanket_and_handkerchiefs_slider)
        )

    def get_blanket_slider_input(self):
        return self.wait.until(
            EC.presence_of_element_located(self.blanket_and_handkerchiefs_input)
        )

    def click_on_blanket_and_handkerchiefs_slider(self):
        self.get_blanket_and_handkerchiefs_slider().click()

    def get_ice_cream_counter_plus_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.ice_cream_counter_plus_button)
        )

    def get_ice_cream_counter_plus_value(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ice_cream_counter_plus_value)
        )

    def click_on_ice_cream_counter_plus_button(self):
        self.get_ice_cream_counter_plus_button().click()

    def get_book_taxi_button(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.book_taxi_button)
        )

    def click_on_book_taxi_button(self):
        self.get_book_taxi_button().click()

    def get_car_search_timer(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.car_search_timer)
        )

    def get_driver_details_after_timer(self):
        WebDriverWait(self.driver, 40).until(
            EC.invisibility_of_element_located(self.car_search_timer)
        )
        return self.wait.until(
            EC.visibility_of_element_located(self.driver_details)
        )





