import os
from playwright.sync_api import expect, Page
from faker import Faker
fake = Faker()

def test_registration(page: Page, fake_credentials):
    email = fake_credentials["email"]
    password = fake_credentials["password"]

    page.goto(os.getenv("REGISTRATION_PAGE"))
    page.wait_for_load_state()

    expect(page.locator("div.component-wrapper")).to_be_visible()

    expect(page.locator("input#name")).to_be_visible()
    page.locator("input#name").fill(fake.name())

    expect(page.locator("select#country")).to_be_visible()
    page.locator("select#country").select_option(fake.country())

    expect(page.locator("select#account")).to_be_visible()
    page.locator("select#account").select_option("Engineer")

    expect(page.locator("input#email")).to_be_visible()
    page.locator("input#email").fill(email)

    expect(page.locator("input#password")).to_be_visible()
    page.locator("input#password").fill(password)

    expect(page.locator("input#confirm_password")).to_be_visible()
    page.locator("input#confirm_password").fill(password)

    expect(page.locator("button[type='submit']")).to_be_visible()
    page.locator("button[type='submit']").click()

    # page.wait_for_timeout(50000)

