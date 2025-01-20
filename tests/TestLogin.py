import time

import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin():

    def test_login(self):
        login=LoginPage(self.driver)
        login.enterEmail("admin@email.com")
        login.enterPassword("admin@123")
        login.clickLogin()
        time.sleep(5)
        home=HomePage(self.driver)
        welcomeMessage=home.get_welcome_text()
        assert "Welcome" in welcomeMessage