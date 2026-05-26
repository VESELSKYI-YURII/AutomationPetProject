import subprocess, pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from faker import Faker
fake = Faker()
load_dotenv()

@pytest.fixture(scope="session")
def fake_credentials():
    email = fake.email()
    password = fake.password()
    print(email, password)
    return {"email":email, "password":password}

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = browser.new_page()
        yield page
        context.close()
        browser.close()
