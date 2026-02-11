"""
Test data configuration for Urban Routes automated tests.

This module contains all test data used across the test suite,
including URLs, addresses, contact information, and payment details.

Attributes:
    urban_routes_url: Base URL of the Urban Routes application
    address_from: Pickup location address
    address_to: Destination address
    phone_number: Phone number for verification
    card_number: Credit card number for payment
    card_code: Credit card CVV code
    message_for_driver: Comment text for the driver
"""

urban_routes_url = 'https://cnt-c1a077da-9736-4f4a-b7a5-1c4417659b03.containerhub.tripleten-services.com?lng=en'
address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
(card_number, card_code) = '1234 5678 9100', '111'
message_for_driver = 'I am wearing red'
