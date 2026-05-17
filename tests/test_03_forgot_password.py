import os
from playwright.sync_api import expect, Page

def test_forgot_password(page: Page, fake_credentials) -> None:
    email = fake_credentials["email"]

    page.goto(os.getenv("FORGOT_PASSWORD_PAGE"))

    expect(page.locator("div.component-wrapper")).to_be_visible()

    expect(page.get_by_placeholder("eg. user@user.com")).to_be_visible()
    expect(page.locator("input#email")).to_be_visible()

    expect(page.locator("button[type='submit']")).to_be_visible()
    page.locator("button[type='submit']").click()

    expect(page.locator("div.form-group p")).to_have_text("Email is a required field")

    page.locator("input#email").fill("test_test@")
    expect(page.locator("div.form-group p")).to_have_text("Email must be a valid email")

    page.locator("input#email").fill(email)

    page.locator("button[type='submit']").click()

