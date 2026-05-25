from pages.registration_page import RegistrationPage

def test_registration(page, fake_credentials):
    register = RegistrationPage(page)

    email = fake_credentials["email"]
    password = fake_credentials["password"]

    register.check_error_messages()
    register.registration(email, password)
