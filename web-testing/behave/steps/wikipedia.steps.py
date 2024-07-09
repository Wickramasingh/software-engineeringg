from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

@given(u'we have navigated to the wikipedia main page') # type: ignore
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(f"http://www.wikipedia.org")
    assert "Wikipedia" in context.browser.title


@when(u'we enter "{invention}" and click on the search button') # type: ignore
def step_impl(context, invention):
    search_element = context.browser.find_element(by=By.ID,value="searchInput")
    search_element.send_keys(invention)
    search_button = context.browser.find_element(by=By.CLASS_NAME, value="pure-button-primary-progressive")
    search_button.click()

@then(u'the resulting page will include "{inventor}"') # type: ignore
def step_impl(context, inventor):
    assert inventor in context.browser.page_source
    sleep(2)
    context.browser.close()

