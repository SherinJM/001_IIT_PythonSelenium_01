from base.SeleniumDriver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    emailFieldValue="//input[@name='email1']"
    passwordFieldValue="//input[@name='password1']"
    submitButtonValue="//button[contains(text(),'Sign in')]"

    def enterEmail(self,email):
        self.waitForElement(self.emailFieldValue,"xpath",30,1)
        self.typeElement(email,self.emailFieldValue,"xpath")

    def enterPassword(self,password):
        self.waitForElement(self.passwordFieldValue,"xpath",30,1)
        self.typeElement(password,self.passwordFieldValue,"xpath")

    def clickLogin(self):
        self.waitForElement(self.submitButtonValue,"xpath",30,1)
        self.clickElement(self.submitButtonValue,"xpath")




