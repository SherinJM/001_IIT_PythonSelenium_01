from base.SeleniumDriver import SeleniumDriver

class HomePage(SeleniumDriver):
    welcome_field="welcomeMessage"
    side_menu="//img[@alt='menu']"
    logout_field="//button[normalize-space()='Sign out']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def get_welcome_text(self):
        self.waitForElement(self.welcome_field,"class",30,1)
        element = self.getElement(self.welcome_field, "class")
        if element:
            return element.text
        else:
            self.log.warning(f"Element with locator '{self.welcome_field}' not found")
            return None