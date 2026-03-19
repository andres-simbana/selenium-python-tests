# selenium-python-tests

E2E test automation framework built with **Selenium WebDriver** and **pytest**, following the **Page Object Model (POM)** design pattern.

## Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green?style=flat-square&logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-8.x-blue?style=flat-square&logo=pytest)
![CI](https://github.com/Anseb77/selenium-python-tests/actions/workflows/tests.yml/badge.svg)

## Project Structure

```
selenium-python-tests/
├── .github/workflows/     # CI/CD with GitHub Actions
├── pages/                 # Page Object Model classes
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── test_login.py
│   └── test_inventory.py
├── conftest.py            # Shared fixtures (WebDriver setup)
├── requirements.txt
└── pytest.ini
```

## Test Coverage

| Module    | Test Cases                                                      |
|-----------|-----------------------------------------------------------------|
| Login     | Valid login, invalid credentials, empty fields, locked user     |
| Inventory | Items count, add to cart, cart badge update                     |

## Setup

```bash
pip install -r requirements.txt
pytest
```

Reports are generated in `reports/report.html`.

## CI

Tests run automatically on every push and pull request via GitHub Actions.
