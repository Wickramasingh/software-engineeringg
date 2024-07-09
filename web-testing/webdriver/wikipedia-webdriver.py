from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# browser = webdriver.Chrome()
# invention = "Telephone"
# browser.get(f"http://www.wikipedia.org/wiki/{invention}")
# assert "Alexander Graham Bell" in browser.page_source
# sleep(10)
# browser.close()

def test_inventor(invention, inventor):
    browser = webdriver.Chrome()
    browser.get(f"http://www.wikipedia.org/wiki/{invention}")
    assert inventor in browser.page_source
    sleep(2)
    browser.close()
    print(f"Found {inventor} for {invention}.")

if __name__ == "__main__":
    test_inventor("Telephone","Alexander Graham Bell")
    test_inventor("Transistor","Bardeen")
    print("done.")
