<div align="center">
  
# 🚖 Urban Routes Project
### Selenium Automated Testing

![Python](https://img.shields.io/badge/Python-3.14.-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.40.-green?style=for-the-badge&logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-9.0.-orange?style=for-the-badge&logo=pytest)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

--- 

## Project Description

This project contains end-to-end automated tests for the **Urban Routes** application, a taxi booking service. The tests verify the complete user flow from route selection to taxi reservation confirmation, including preference configuration, payment methods, and special trip requirements.

The project implements the **Page Object Model (POM)** design pattern to keep test code organized, maintainable, and reusable.

---

## Technologies and Techniques Used

### Technologies
- **Python 3.14.0** - Primary programming language
- **Selenium WebDriver 4.40.0** - Web browser automation framework
- **Pytest 9.0.0** - Python testing framework
- **ChromeDriver** - Driver for Google Chrome automation

### Techniques and Patterns
- **Page Object Model (POM)** - Design pattern to separate test logic from UI interaction
- **Explicit Waits** - Explicit waits to handle dynamic elements
- **XPath and CSS Selectors** - Element location strategies
- **Expected Conditions** - Wait conditions for element synchronization
- **Class-based Test Organization** - Test organization in classes for better structure

---

## Project Structure
```
urban_routes_project/
│
├── pages/
│   └── urban_routes_pages.py    # Page Object with locators and methods
│
├── tests/
│   └── urban_routes_tests.py    # Automated test suite
│
├── utilities/
│   └── retrieve_code.py         # Utility to retrieve SMS verification code
│
├── data.py                       # Test data (URLs, credentials, inputs)
├── requirements.txt              # Project dependencies
├── .gitignore                    # Files ignored by Git
└── README.md                     # Project documentation
```

---

## Setup and Installation

### Prerequisites
- Python 3.14 or higher
- Google Chrome installed
- ChromeDriver compatible with your Chrome version

### Installation

1. **Clone the repository**
```bash
   git clone <repository-url>
   cd Qa-Selenium-Project-Urban-Routes
```

2. **Create virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

---

## Running Tests

### Run all tests
```bash
pytest tests/urban_routes_tests.py
```

### Run a specific test
```bash
pytest tests/urban_routes_tests.py::TestUrbanRoutes::test_set_route
```

### Run with detailed output
```bash
pytest tests/urban_routes_tests.py -v
```

---

## Test Cases

The project includes 9 automated tests covering the complete booking flow:

| # | Test Case | Description |
|---|-----------|-------------|
| 1 | `test_set_route` | Set pickup and drop-off addresses |
| 2 | `test_comfort_fare` | Select Comfort fare option |
| 3 | `test_add_phone_number` | Add and verify phone number |
| 4 | `test_add_credit_card` | Add credit card as payment method |
| 5 | `test_comment_for_driver` | Add comment for the driver |
| 6 | `test_add_blanket_and_handkerchiefs` | Enable blanket and handkerchiefs option |
| 7 | `test_add_ice_cream` | Add ice cream to the order |
| 8 | `test_car_search_modal` | Verify taxi search modal appears |
| 9 | `test_driver_info_appears` | Verify driver information appears |

---

## Sample Test Results
```
========================= test session starts =========================
collected 9 items

tests/urban_routes_tests.py::TestUrbanRoutes::test_set_route PASSED      [ 11%]
tests/urban_routes_tests.py::TestUrbanRoutes::test_comfort_fare PASSED   [ 22%]
tests/urban_routes_tests.py::TestUrbanRoutes::test_add_phone_number PASSED [ 33%]
tests/urban_routes_tests.py::TestUrbanRoutes::test_add_credit_card PASSED [ 44%]
tests/urban_routes_tests.py::TestUrbanRoutes::test_comment_for_driver PASSED [ 55%]
tests/urban_routes_tests.py::TestUrbanRoutes::test_add_blanket_and_handkerchiefs PASSED [ 66%]
tests/urban_routes_tests.py::TestUrbanRoutes::test_add_ice_cream PASSED [ 77%]
tests/urban_routes_tests.py::TestUrbanRoutes::test_car_search_modal PASSED [ 88%]
tests/urban_routes_tests.py::TestUrbanRoutes::test_driver_info_appears PASSED [100%]

========================= 9 passed in 45.23s =========================
```

---

## Configuration

Test data is configured in `data.py`:
```python
urban_routes_url = 'https://...'
address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
card_number = '1234 5678 9100'
card_code = '111'
message_for_driver = 'I am wearing red'
```

---

## Important Notes

- Tests run **sequentially** following the user flow
- A **single browser session** is used for the entire test suite (session scope)
- **Explicit waits** ensure synchronization with dynamic elements
- The **POM pattern** facilitates test maintenance and updates

---

## 👨‍💻 Author

***Camilo — QA Engineer in Training***

📌 *This project was developed as part of my QA Engineering Bootcamp and learning journey and showcases hands-on experience with Selenium WebDriver and automated UI testing.*

If you want to connect:

<p align="left">
  <a href="https://github.com/Jcma14">
    <img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"/>
  </a>
  <br>
    <a href="https://www.linkedin.com/in/camilo-morales-qa/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</p>

**Thank you for reviewing this project!** 🚀
