# selenium-python-tests

![Tests](https://github.com/andres-simbana/selenium-python-tests/actions/workflows/tests.yml/badge.svg)

E2E test automation suite for [SauceDemo](https://www.saucedemo.com/) using **Selenium** and **Pytest**, following the **Page Object Model (POM)** pattern. Includes HTML report generation and CI/CD with GitHub Actions.

---

## 🛠️ Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)

---

## 📁 Project Structure

```
selenium-python-tests/
├── pages/
│   ├── login_page.py       # Login page interactions
│   ├── inventory_page.py   # Product listing page
│   └── cart_page.py        # Shopping cart page
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── conftest.py             # Pytest fixtures (WebDriver setup/teardown)
├── pytest.ini
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/andres-simbana/selenium-python-tests.git
cd selenium-python-tests
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> Make sure you have **Chrome** installed. Selenium 4 manages the driver automatically.

---

## ▶️ Running the tests

Run all tests:
```bash
pytest
```

Run a specific test file:
```bash
pytest tests/test_login.py
```

Run with verbose output:
```bash
pytest -v
```

---

## 📊 HTML Report

After running, the report is generated at:
```
reports/report.html
```

Open it in any browser to see detailed results.

---

## 🔄 CI/CD

Tests run automatically on every push via **GitHub Actions** (`.github/workflows/tests.yml`).
