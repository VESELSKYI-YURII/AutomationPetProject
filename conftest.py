import subprocess, pytest
from faker import Faker
from playwright.sync_api import sync_playwright

fake = Faker()

@pytest.fixture(scope="session")
def fake_credentials():
    email = fake.email()
    password = fake.password()
    print(email, password)
    return {"email":email, "password":password}

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = browser.new_page()
        yield page
        context.close()
        browser.close()
