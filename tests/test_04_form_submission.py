from pages.form_submission_page import FormSubmissionPage

def test_form_submission(page):
    form = FormSubmissionPage(page)

    form.fill_form_submission()
    form.check_success_message()