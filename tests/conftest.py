import pytest

from base.WebDriverFactory import WebDriverFactory

@pytest.fixture(scope="class")
def setup(request):

    wdf=WebDriverFactory("chrome")
    driver=wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver=driver
    print("Application is up and running...")
    yield driver
    driver.quit()
    print("Closing the browser...")
