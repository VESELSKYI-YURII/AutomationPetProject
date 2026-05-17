from playwright.sync_api import expect
from pages.base_page import BasePage
import os
from faker import Faker
fake = Faker()

class RegistrationPage(BasePage):

    # Locators
    name_input = lambda self: self.page.locator("input#name")
    country_dropdown_menu = lambda self: self.page.locator("select#country")
    account_type_menu = lambda self: self.page.locator("select#account")
    email_input = lambda self: self.page.locator("input#email")
    password_input = lambda self: self.page.locator("input#password")
    confirm_password_input = lambda self: self.page.locator("input#confirm_password")
    submit_button  = lambda self: self.page.locator("button[type='submit']")
    title_in_the_form = lambda self: self.page.locator("div.component-wrapper")

    # Errors
    name_input_error = lambda self: self.page.locator("div.form-group p").first
    country_dropdown_menu_error = lambda self: self.page.locator("div.form-group p").nth(1)
    account_type_menu_error = lambda self: self.page.locator("div.form-group p").nth(2)
    email_input_error = lambda self: self.page.locator("div.form-group p").nth(3)
    password_input_error = lambda self: self.page.locator("div.form-group p").nth(4)
    confirm_password_input_error = lambda self: self.page.locator("div.form-group p").last


    def open(self):
        self.goto(os.getenv("REGISTRATION_PAGE_URL"))
        self.page.wait_for_load_state()
        expect(self.title_in_the_form()).to_be_visible()

    def registration(self, email, password):
        # self.open()
        self.name_input().fill(fake.name())
        self.country_dropdown_menu().select_option(fake.country())
        self.account_type_menu().select_option("Engineer")
        self.email_input().fill(email)
        self.password_input().fill(password)
        self.confirm_password_input().fill(password)
        self.submit_button().click()

    def check_error_messages(self):
        self.open()
        self.submit_button().click()
        expect(self.name_input_error()).to_have_text("Name is a required field")
        expect(self.country_dropdown_menu_error()).to_have_text("Country is a required field")
        expect(self.account_type_menu_error()).to_have_text("Account is a required field")
        expect(self.email_input_error()).to_have_text("Email is a required field")
        expect(self.password_input_error()).to_have_text("Password is a required field")
        expect(self.confirm_password_input_error()).to_have_text("Confirm Password is required")