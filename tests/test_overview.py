import pytest
from pages.overview_page import OverviewPage


@pytest.mark.smoke
@pytest.mark.ui
def test_go_to_tools(logged_in_page):
    page = logged_in_page
    overview = OverviewPage(page)

    overview.go_to_tools()

    assert "tools" in page.url
    


@pytest.mark.smoke
@pytest.mark.ui
def test_tools_count_test_overview_count_equal(logged_in_page):
    page = logged_in_page
    overview = OverviewPage(page)

    overview.go_to_tools()
    tools_install, tools_enabled, tools_disabled = overview.get_tools_count()
    page.screenshot(path="before_overview.png")
    overview.go_to_overview()
    overview_install, overview_enabled, overview_disabled = overview.get_overview_counts()

    assert overview_install == tools_install
    assert overview_enabled == tools_enabled
    assert overview_disabled == tools_disabled