from pages.base_page import BasePage
from playwright.sync_api import expect
import os
from faker import Faker
fake = Faker()

class FormSubmissionPage(BasePage):

    # Locators
    name_input = lambda self: self.page.locator("input#name")
    email_input = lambda self: self.page.locator("input#email")
    contact_number_input = lambda self: self.page.locator("input#contact")
    date_input = lambda self: self.page.locator("input#date")
    cv_input = lambda self: self.page.locator("input#file")
    color = lambda self: self.page.locator("div.form-group div div").first
    menu = lambda self: self.page.locator("div.form-group div div").last
    country_dropdown_menu = lambda self: self.page.locator("div.form-group select#country")
    submit_button  = lambda self: self.page.locator("button[type='submit']")

    #Success messages
    success_message = lambda self: self.page.locator("div#success-msg")
    second_success_message = lambda self: self.page.locator("div#success-msg span").first
    text_in_second_success_message = lambda self: self.page.locator("div#success-msg h2")

    def open(self):
        self.goto(os.getenv("FORM_SUBMISSION_PAGE"))
        self.page.wait_for_load_state()

    def fill_form_submission(self):
        self.name_input().fill(fake.name())
        self.email_input().fill(fake.email())
        self.contact_number_input().fill(fake.msisdn())
        self.date_input().fill(fake.date())
        self.cv_input().set_input_files("./files/Yurii-Veselskyi-QA-CV.pdf")
        self.color().locator("input#Red").check()
        self.menu().locator("input#Pasta").check()
        self.menu().locator("input#Sandwich").check()
        self.country_dropdown_menu().select_option(fake.country())
        self.submit_button().click()

    def check_success_message(self):
        expect(self.success_message()).to_be_visible()
        expect(self.second_success_message()).to_have_text("Form submit successfully.")
        expect(self.text_in_second_success_message()).to_have_text("successfully submitted")