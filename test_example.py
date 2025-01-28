from playwright.sync_api import Page
from reportportal_client import RPLogger

def test_amazon_search(rp_logger: RPLogger, page: Page):
    page.goto("https://www.amazon.com/")
    page.get_by_placeholder("Search Amazon").fill("Galaxy")
    page.get_by_role("button", name="Go", exact=True).click()


