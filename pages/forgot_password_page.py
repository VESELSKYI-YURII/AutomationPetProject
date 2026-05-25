from pages.base_page import BasePage
from playwright.sync_api import expect
import os

class ForgetPasswordPage(BasePage):

    # Locators
    email_input = lambda self: self.page.locator("input#email")
    submit_button = lambda self: self.page.locator("button[type=submit]")
    title_in_the_form = lambda self: self.page.locator("div.component-wrapper h2")

    #Success messages
    success_frame = lambda self: self.page.locator("div#success-msg")
    first_success_message = lambda self: self.page.locator("div#success-msg span").first
    second_success_message = lambda self: self.page.locator("div#success-msg p")

    def open(self):
        self.goto(os.getenv("FORGOT_PASSWORD_PAGE"))

    def send_forgot_password_email(self):
        expect(self.title_in_the_form()).to_be_visible()
        self.email_input().fill(os.getenv("EMAIL"))
        self.submit_button().click()

    def check_success_message(self):
        expect(self.success_frame()).to_be_visible()
        expect(self.first_success_message()).to_have_text("Password is reset successfully.")
        expect(self.second_success_message()).to_contain_text(os.getenv("EMAIL"))
