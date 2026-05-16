import os
from playwright.sync_api import expect, Page



def test_login(page: Page):
    page.goto(os.getenv("LOGIN_PAGE"))
    page.wait_for_load_state()

    expect(page.locator("div.component-wrapper")).to_be_visible()

    expect(page.locator("div#guide-lines")).to_be_visible()

    expect(page.locator("input#email")).to_be_visible()
    page.locator("input#email").fill(os.getenv("EMAIL"))

    expect(page.locator("input#password")).to_be_visible()
    page.locator("input#password").fill(os.getenv("PASSWORD"))

    expect(page.locator("button[type='button']").nth(2)).to_be_visible()
    page.locator("button[type='button']").nth(2).click()

    expect(page.locator("button[type='submit']")).to_be_visible()
    page.locator("button[type='submit']").click()

    expect(page.locator("div#success-msg")).to_be_visible()

    expect(page.locator("div#success-msg svg").first).to_be_visible()
    expect(page.locator("div#success-msg span").first).to_have_text("Login Successful")
    expect(page.locator("div#success-msg h2")).to_have_text("Login Successful")

    expect(page.get_by_role("button", name="Logout")).to_be_visible()
    page.get_by_role("button", name="Logout").click()

    expect(page.locator("input#email")).to_be_visible()
    expect(page.locator("input#password")).to_be_visible()
    expect(page.locator("button[type='submit']")).to_be_visible()

    page.close()




