from selenium import webdriver

class WebDriverFactory():
    def __init__(self,browser):
        self.browser=browser

    def getWebDriverInstance(self):
        baseurl="https://freelance-learn-automation.vercel.app/login"

        if self.browser=="chrome":
            driver=webdriver.Chrome()
        elif self.browser=="edge":
            driver=webdriver.Edge()
        elif self.browser=="firefox":
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Chrome()

        driver.implicitly_wait(10)
        driver.set_page_load_timeout(60)
        driver.set_script_timeout(10)
        driver.maximize_window()
        driver.get(baseurl)

        return driver


