import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver_init(request):
    # Initialize the WebDriver (Chrome)
    driver = webdriver.Chrome()

    # Assign the driver to the test class instance
    request.cls.driver = driver

    # Yield the driver object to the test functions
    yield driver

    # Quit the WebDriver after the test class is done
    driver.quit()
