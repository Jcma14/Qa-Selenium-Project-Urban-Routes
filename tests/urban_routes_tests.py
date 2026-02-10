from data import data
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_pages import UrbanRoutesPage
from selenium import webdriver


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance":"ALL"})
        cls.driver = webdriver.Chrome(service=Service(),options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)


    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_comfort_fare(self):
        self.routes_page.click_on_call_taxi_button()
        self.routes_page.click_on_comfort_fare()
        comfort_fare = self.routes_page.get_comfort_fare()
        comfort_text = "Comfort"
        assert comfort_fare.text == comfort_text

    def test_add_phone_number(self):
        self.routes_page.click_on_phone_number_button()
        self.routes_page.set_phone_number_field(data.phone_number)
        self.routes_page.click_on_next_button()
        self.routes_page.set_sms_code()
        self.routes_page.click_on_confirmation_button()
        assert self.routes_page.get_phone_number_after_confirmation() == data.phone_number

    def test_add_credit_card(self):
        self.routes_page.click_on_payment_method_button()
        self.routes_page.click_on_add_card_button()
        self.routes_page.set_card_number_field()
        self.routes_page.set_card_code_field()
        self.routes_page.click_on_add_card_submit_button()
        assert self.routes_page.get_new_card_added().is_displayed()
        self.routes_page.click_on_payment_method_close_button()

    def test_comment_for_driver(self):
        self.routes_page.set_comment_for_driver_field()
        assert self.routes_page.get_comment_for_driver_value() == data.message_for_driver

    def test_add_blanket_and_handkerchiefs(self):
        assert self.routes_page.get_order_requirements_button().is_enabled()
        self.routes_page.click_on_blanket_and_handkerchiefs_slider()
        assert self.routes_page.get_blanket_slider_input().is_selected()

    def test_add_ice_cream(self):
        self.routes_page.click_on_ice_cream_counter_plus_button()
        self.routes_page.click_on_ice_cream_counter_plus_button()
        assert self.routes_page.get_ice_cream_counter_plus_value().text == '2'

    def test_car_search_modal(self):
        self.routes_page.click_on_book_taxi_button()
        assert self.routes_page.get_car_search_timer().is_displayed()

    def test_driver_info_appears(self):
        assert self.routes_page.get_driver_details_after_timer().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
