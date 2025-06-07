from selenium import webdriver
from selenium.webdriver.common.by import By
from genai_healer.wrapper import try_genai_find_element

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")  # replace with your actual test page

# Intentionally using a broken locator
element = try_genai_find_element(
    driver,
    By.XPATH,
    "//*[@name = 'usern']",  # Broken locator
    module="test_login",  # Tag used for fallback memory
    html_snippet="<button>Submit</button>"  # Optional DOM context
)

element.click()
driver.quit()
