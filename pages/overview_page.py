import logging
import allure

logger = logging.getLogger(__name__)

class OverviewPage:

    def __init__(self, page):
        self.page = page

        self.account_menu = page.locator("a:has-text('Account') img.arrow-icon")
        self.tools_link = page.locator("a:has-text('Tools')")
        self.overview_link = self.page.locator('li[routerlink="./dashboard"]')
        self.tools_cards = page.locator(".tab-display-grid .add-on-tabs-grid")
        self.badges = page.locator(".px-badge")
 
    @allure.step("Navigate to Tool page")
    def go_to_tools(self):
        logger.info("Navigating to Tools page")
        self.account_menu.click()
        self.tools_link.click()
        self.page.wait_for_load_state("networkidle")
        
        
    @allure.step("Navigate to Overview page")
    def go_to_overview(self):
        
        self.overview_link.wait_for(state="visible")
        self.overview_link.click()
        self.page.wait_for_load_state("networkidle")
 
    @allure.step("Fetch tools count")
    def get_tools_count(self):
        logger.info("Fetching tools count")
        install = enabled = disabled = 0

        for tool in self.tools_cards.all():
            if tool.locator("button:has-text('Install')").is_visible():
                install += 1
            elif tool.locator(".tab-tag-enabled").is_visible():
                enabled += 1
            elif tool.locator(".tab-tag-disabled").is_visible():
                disabled += 1

        logger.info(f"Tools → Install:{install}, Enabled:{enabled}, Disabled:{disabled}")
        return install, enabled, disabled
    
    @allure.step("Fetch overview tools count")
    def get_overview_counts(self):
        logger.info("Fetching overview badge counts")

        overview_enabled = overview_disabled = overview_install = 0

        for i in range(self.badges.count()):
            badge = self.badges.nth(i)
            color = badge.get_attribute("style")
            count = int(badge.inner_text().strip())

            if "#006E42" in color:
                overview_enabled = count
            elif "#F9B702" in color:
                overview_disabled = count
            elif "#8A9199" in color:
                overview_install = count

        logger.info(f"Overview → Install:{overview_install}, Enabled:{overview_enabled}, Disabled:{overview_disabled}")
        return overview_install, overview_enabled, overview_disabled

    @allure.step("Install tool button checking")
    def click_install_tools(self):
        logger.info("Clicking Install Tools button")
        self.page.locator("button.install-tools").click()
        self.page.wait_for_load_state("networkidle")
        
    @allure.step("tool page is loading")
    def is_tools_page_loaded(self):
        logger.info("Validating Tools page loaded")
        return self.page.get_by_role("heading", name="Available Tools").is_visible()