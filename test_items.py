import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_must_have_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(5)  
    button1 = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button1.is_enabled(), "btn-add-to-basket is not enabled"
    print("\ntest_must_have_button_add_to_basket IS FINISHED")