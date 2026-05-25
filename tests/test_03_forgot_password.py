from pages.forgot_password_page import ForgetPasswordPage

def test_forgot_password(page):
    forgot_password = ForgetPasswordPage(page)

    forgot_password.open()
    forgot_password.send_forgot_password_email()
    forgot_password.check_success_message()

