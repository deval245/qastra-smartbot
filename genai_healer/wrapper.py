from selenium.common.exceptions import NoSuchElementException
from genai_healer.locator_healer import heal_locator

def try_genai_find_element(driver, by, locator, module="default", html_snippet=None):
    try:
        return driver.find_element(by, locator)
    except NoSuchElementException:
        healed = heal_locator(locator, module, html_snippet)
        if healed:
            return driver.find_element(by, healed)
        else:
            raise Exception("Locator healing failed.")
