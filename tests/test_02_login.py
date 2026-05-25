from pages.login_page import LoginPage
import os

def test_login(page, fake_credentials):
    login = LoginPage(page)

    login.login(os.getenv("EMAIL"),os.getenv("PASSWORD"),)
    login.check_success_message()
    login.logout()




