from pages.base_page import BasePage
from playwright.sync_api import expect
import os

class LoginPage(BasePage):

    # Locators
    email_input = lambda self: self.page.locator("input#email")
    password_input = lambda self: self.page.locator("input#password")
    submit_button = lambda self: self.page.locator("button[type=submit]")
    title_in_the_form = lambda self: self.page.locator("div.component-wrapper")
    guide_line_info = lambda self: self.page.locator("div#guide-lines")
    logout_button = lambda self: self.page.get_by_role("button", name="Logout")

    #Success messages
    success_message = lambda self: self.page.locator("div#success-msg")
    second_success_message = lambda self: self.page.locator("div#success-msg span").first
    text_in_second_success_message = lambda self: self.page.locator("div#success-msg h2").first


    def open(self):
        self.goto(os.getenv("LOGIN_PAGE_URL"))
        self.page.wait_for_load_state()
        expect(self.title_in_the_form()).to_be_visible()
        expect(self.guide_line_info()).to_be_visible()

    def login(self, email, password):
        self.open()
        self.email_input().fill(email)
        self.password_input().fill(password)
        self.submit_button().click()

    def check_success_message(self):
        expect(self.success_message()).to_be_visible()
        expect(self.second_success_message()).to_have_text("Login Successful")
        expect(self.text_in_second_success_message()).to_have_text("Login Successful")

    def logout(self):
        self.logout_button().click()
        expect(self.email_input()).to_be_visible(timeout=10000)
        expect(self.password_input()).to_be_visible()
        expect(self.submit_button()).to_be_visible()