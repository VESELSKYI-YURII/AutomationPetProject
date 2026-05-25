from pages.base_page import BasePage
from playwright.sync_api import expect
import os

class DragAndDropListPage(BasePage):

    # Locators
    drag_element = lambda self: self.page.locator("div.component-wrapper div div").first
    drop_element = lambda self: self.page.locator("div.component-wrapper div div").last
    title_in_the_form = lambda self: self.page.locator("div.component-wrapper h2")
    title_in_the_drop_element = lambda self: self.page.locator("div.component-wrapper h3")
    dropped_element = lambda self: self.page.locator("div.component-wrapper div").last



    def open(self):
        self.goto(os.getenv("DRAG_AND_DROP_PAGE"))

    def drag_and_drop(self):
        self.page.wait_for_timeout(2000)
        expect(self.drop_element()).to_have_text("Drop Here")
        self.drag_element().drag_to(self.drop_element())

    def check_drag_and_drop_list(self):
        expect(self.title_in_the_form()).to_be_visible()
        expect(self.title_in_the_drop_element()).to_have_text("Dropped!")
        expect(self.dropped_element()).to_have_text("Drag Me")
