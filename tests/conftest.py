import pytest
import logging
from pages.login_page import LoginPage
from utils.data_reader import get_login_data
from playwright.sync_api import expect
import allure


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


@pytest.fixture
def logged_in_page(page):
    logger.info("Starting login fixture")

    data = get_login_data()
    login_page = LoginPage(page)

    logger.info("Opening login page")
    login_page.load()

    logger.info("Performing login")
    login_page.login(
        data["account_number"],
        data["username"],
        data["password"]
    )

    logger.info("Validating successful login")
    expect(
        page.get_by_role("listitem").filter(has_text="Overview")
    ).to_be_visible()

    # Attach screenshot to Allure
    allure.attach(
        page.screenshot(),
        name="Login Successful",
        attachment_type=allure.attachment_type.PNG
    )

    logger.info("Login successful")

    yield page

    logger.info("Test finished")


# ⬇️ ADD THIS BELOW THE FIXTURE
def pytest_runtest_makereport(item, call):

    if call.when == "call" and call.excinfo is not None:

        page = item.funcargs.get("page")

        if not page:
            page = item.funcargs.get("logged_in_page")

        if page:
            allure.attach(
                page.screenshot(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )