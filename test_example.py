from playwright.sync_api import Page
from reportportal_client import RPLogger

def test_amazon_search(rp_logger: RPLogger, page: Page):
    rp_logger.info("Hello world!")
    page.goto("https://www.amazon.com/")
    page.get_by_placeholder("Search Amazon").fill("Galaxy")
    page.get_by_role("button", name="Go", exact=True).click()


def test_zap_search(rp_logger: RPLogger, page: Page):
    rp_logger.info("zap.co.il search")
    page.goto("https://www.zap.co.il/")
    page.get_by_role("textbox", name="אני רוצה לקנות").fill("טלויזיה")
    page.locator(".typedInput__match").first.click()
    page.get_by_role("link", name="Samsung", exact=True).click()