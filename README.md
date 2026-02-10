<div align="center">

# 🚖 Urban Routes Project

### Selenium WebDriver Automated Tests

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python\&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium\&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-Testing-yellow?logo=pytest\&logoColor=white)
![PyCharm](https://img.shields.io/badge/IDE-PyCharm-darkgreen?logo=pycharm\&logoColor=white)

</div>

---

## Project Description

**Urban Routes Project** is a Selenium-based automation project created to test the *Urban Routes* web application. The goal of this project is to validate critical user flows such as route selection, driver assignment, and dynamic UI behavior using reliable and maintainable automated tests.

The project follows good QA automation practices, focusing on readable locators, reusable methods, and robust synchronization for dynamic elements like timers and modals.

---

## What’s Included

* Automated end-to-end test scenarios for the Urban Routes web app
* Well-structured locators for dynamic and static elements
* Reusable helper methods (getters, setters, click actions)
* Assertions to validate UI behavior and loaded data
* Handling of dynamic content such as timers and modal dialogs

---

## Technologies & Techniques Used

### Technologies

* **Python** – Main programming language
* **Selenium WebDriver** – Browser automation
* **PyTest** – Test execution and assertions
* **PyCharm** – Development environment

### Techniques & Practices

* **Page Object Model (POM)** for clean test structure
* **XPath & class-based locators** for element identification
* **Explicit waits (WebDriverWait)** for dynamic UI handling
* **Custom wait conditions** for timers and delayed content
* **Assertions** to validate presence, visibility, and correctness of data

---

## How to Run the Tests

### Prerequisites

Make sure you have the following installed on your system:

* **Python 3.x**
* **Google Chrome** (or another supported browser)
* **ChromeDriver** compatible with your browser version
* **pip** (Python package manager)

### Running the Tests

To execute all automated tests, run:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/test_urban_routes.py
```

### Notes

* Tests use **explicit waits** to handle dynamic elements such as timers and modal dialogs.
* Make sure the application under test is accessible before running the tests.

---

## Purpose

This project demonstrates practical Selenium automation skills, including working with real-world asynchronous behavior, creating maintainable test code, and validating user-facing functionality in a modern web application.

---

📌 *This project was developed as part of my QA Engineering Bootcamp and learning journey and showcases hands-on experience with Selenium WebDriver and automated UI testing.*
