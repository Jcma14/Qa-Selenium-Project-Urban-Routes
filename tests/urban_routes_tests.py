from data import data
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_pages import UrbanRoutesPage
from selenium import webdriver


class TestUrbanRoutes:
    """
    Test suite for Urban Routes taxi booking application.
    
    This test class contains end-to-end tests that verify the complete
    user flow for booking a taxi, including route selection, fare choice,
    payment setup, preferences, and booking confirmation.
    
    Tests are executed sequentially as they represent a single user journey.
    """

    driver = None

    @classmethod
    def setup_class(cls):
        """
        Set up the test environment before running tests.
        
        Initializes Chrome WebDriver with performance logging enabled,
        navigates to the Urban Routes URL, and creates a page object instance.
        This runs once before all tests in the class.
        """
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance":"ALL"})
        cls.driver = webdriver.Chrome(service=Service(),options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)


    def test_set_route(self):
        """
        Test that user can set pickup and drop-off addresses.
        
        Verifies that:
        - Pickup address can be entered and retrieved correctly
        - Destination address can be entered and retrieved correctly
        """
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_comfort_fare(self):
        """
        Test that user can select the Comfort fare option.
        
        Verifies that:
        - Comfort fare option can be clicked
        - Comfort fare is properly selected and displayed
        """
        self.routes_page.click_on_call_taxi_button()
        self.routes_page.click_on_comfort_fare()
        comfort_fare = self.routes_page.get_comfort_fare()
        comfort_text = "Comfort"
        assert comfort_fare.text == comfort_text

    def test_add_phone_number(self):
        """
        Test that user can add and verify a phone number.
        
        Verifies that:
        - Phone number input field accepts the number
        - SMS verification code can be retrieved and entered
        - Phone number is confirmed and displayed after verification
        """
        self.routes_page.click_on_phone_number_button()
        self.routes_page.set_phone_number_field(data.phone_number)
        self.routes_page.click_on_next_button()
        self.routes_page.set_sms_code()
        self.routes_page.click_on_confirmation_button()
        assert self.routes_page.get_phone_number_after_confirmation() == data.phone_number

    def test_add_credit_card(self):
        """
        Test that user can add a credit card as payment method.
        
        Verifies that:
        - Payment method modal can be opened
        - Card number and CVV code can be entered
        - Card is successfully added and appears in payment methods list
        """
        self.routes_page.click_on_payment_method_button()
        self.routes_page.click_on_add_card_button()
        self.routes_page.set_card_number_field()
        self.routes_page.set_card_code_field()
        self.routes_page.click_on_add_card_submit_button()
        assert self.routes_page.get_new_card_added().is_displayed()
        self.routes_page.click_on_payment_method_close_button()

    def test_comment_for_driver(self):
        """
        Test that user can add a comment for the driver.
        
        Verifies that:
        - Comment field accepts text input
        - Comment is properly saved and can be retrieved
        """
        self.routes_page.set_comment_for_driver_field()
        assert self.routes_page.get_comment_for_driver_value() == data.message_for_driver

    def test_add_blanket_and_handkerchiefs(self):
        """
        Test that user can enable the blanket and handkerchiefs option.
        
        Verifies that:
        - Toggle slider can be clicked
        - Option is properly enabled (checked state)
        """
        assert self.routes_page.get_order_requirements_button().is_enabled()
        self.routes_page.click_on_blanket_and_handkerchiefs_slider()
        assert self.routes_page.get_blanket_slider_input().is_selected()

    def test_add_ice_cream(self):
        """
        Test that user can add ice cream to the order.
        
        Verifies that:
        - Ice cream quantity can be incremented
        - Counter displays correct quantity after increments
        """
        self.routes_page.click_on_ice_cream_counter_plus_button()
        self.routes_page.click_on_ice_cream_counter_plus_button()
        assert self.routes_page.get_ice_cream_counter_plus_value().text == '2'

    def test_car_search_modal(self):
        """
        Test that taxi search modal appears when booking.
        
        Verifies that:
        - Book taxi button can be clicked
        - Search modal with timer is displayed
        """
        self.routes_page.click_on_book_taxi_button()
        assert self.routes_page.get_car_search_timer().is_displayed()

    def test_driver_info_appears(self):
        """
        Test that driver information appears after search completes.
        
        Verifies that:
        - Search timer completes and disappears
        - Driver details (name, rating) are displayed
        
        Note: This test waits for the search timer to complete (up to 40 seconds).
        """
        assert self.routes_page.get_driver_details_after_timer().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
