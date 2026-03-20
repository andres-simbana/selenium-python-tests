import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.saucedemo.com"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver, base_url):
    login = LoginPage(driver)
    login.open(base_url)
    login.login(VALID_USERNAME, VALID_PASSWORD)
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html"),
        message="Login no redirigió a inventory — verifica credenciales o estado del sitio"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when in ("call", "setup") and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
