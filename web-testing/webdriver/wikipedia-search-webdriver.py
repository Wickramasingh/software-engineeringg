from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_inventor(invention, inventor):
    # Using try-except-finally to ensure browser closes in case of any exceptions
    try:
        # Initialize ChromeDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Optional: Run in headless mode
        driver = webdriver.Chrome(options=chrome_options)

        # Open Wikipedia homepage
        driver.get("https://www.wikipedia.org")

        # Wait for the page title to contain "Wikipedia"
        WebDriverWait(driver, 10).until(EC.title_contains("Wikipedia"))

        # Find the search input element and enter the invention
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )
        search_input.send_keys(invention)

        # Click the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        search_button.click()

        # Wait for the results to load (adjust sleep time as needed)
        sleep(5)

        # Example of verifying the inventor on the results page (adjust as per Wikipedia structure)
        assert inventor in driver.page_source, f"{inventor} not found in page source"

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
    finally:
        # Close the browser session in all cases
        if driver:
            driver.quit()

if __name__ == "__main__":
    test_inventor("Telephone", "Alexander Graham Bell")
    test_inventor("Transistor", "John Bardeen")
    test_inventor("Light Bulb", "Thomas Edison")
    print("Done.")

