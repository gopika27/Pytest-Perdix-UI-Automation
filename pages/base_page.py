import logging

logger = logging.getLogger(__name__)

class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        logger.info(f"Clicking on element: {locator}")
        self.page.locator(locator).click()

    def fill(self, locator, value):
        logger.info(f"Filling {locator} with value")
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        logger.info(f"Getting text from: {locator}")
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        logger.info(f"Checking visibility of: {locator}")
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator):
        logger.info(f"Waiting for element: {locator}")
        self.page.locator(locator).wait_for()