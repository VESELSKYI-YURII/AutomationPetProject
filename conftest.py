import subprocess, pytest
from faker import Faker

fake = Faker()

@pytest.fixture(scope="session")
def fake_credentials():
    email = fake.email()
    password = fake.password()
    return {"email":email, "password":password}

def pytest_sessionfinish():
    subprocess.run(["allure", "generate", "--clean"], check=True)
    subprocess.run(["allure", "open"], check=True)