import logging

from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import utility.CustomLogger as cl


class SeleniumDriver():

    log=cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver

    def getByType(self,locatorType):
        locatorType=locatorType.lower()

        print("Locator type here is: ",locatorType)

        if locatorType=="id":
            return By.ID
        elif locatorType=="name":
            print("I am here")
            return By.NAME
        elif locatorType=="class":
            return By.CLASS_NAME
        elif locatorType=="xpath":
            return By.XPATH
        elif locatorType=="tagName":
            return By.TAG_NAME
        elif locatorType=="linkText":
            return By.LINK_TEXT
        elif locatorType=="partialLinkText":
            return By.PARTIAL_LINK_TEXT
        elif locatorType=="cssSelector":
            return By.CSS_SELECTOR
        else:
            # print("Locator type not supported")
            self.log.info("Locator type "+locatorType+" not supported")

    def getElement(self,locator,locatorType="id"):
        element=None
        try:
            byType=self.getByType(locatorType)
            print("byType is: ",byType)
            print("locator is: ",locator)
            element=self.driver.find_element(byType,locator)
            print("element here is: ",element)
            print("Element Found")
        except:
            print("Element not Found")
        return element

    def clickElement(self,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            element.click()
            print("Clicked on element")
        except:
            print("Cannot click on element")

    def typeElement(self,data,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            print("Element is: ",element)
            element.send_keys(data)
            print("Entered data")
        except:
            print("Cannot type data")

    def waitForElement(self,locator,locatorType,timeout=30,pollFrequency=1):
        element=None
        try:
            element=self.getElement(locator,locatorType)
            wait = WebDriverWait(self.driver, timeout, pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                     ElementClickInterceptedException, ElementNotVisibleException])
            wait.until(expected_conditions.element_to_be_clickable(element))
            print("Element found with explicit wait")
        except:
            print("Element not found with explicit conditions")
        return element

