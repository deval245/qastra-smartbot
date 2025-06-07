from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def capture_dom(url: str) -> str:
    """Launch the browser, capture the page source, and return DOM as HTML."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        html = driver.page_source
    finally:
        driver.quit()

    return html

def extract_locators_from_dom(html: str) -> list:
    """Parse DOM using BeautifulSoup and suggest possible locators."""
    soup = BeautifulSoup(html, 'html.parser')
    suggestions = []

    for tag in soup.find_all(['input', 'button', 'a', 'form', 'label']):
        attrs = tag.attrs
        tag_name = tag.name

        if 'id' in attrs:
            suggestions.append((tag_name, f"//*[@id='{attrs['id']}']"))
        elif 'name' in attrs:
            suggestions.append((tag_name, f"//{tag_name}[@name='{attrs['name']}']"))
        elif 'placeholder' in attrs:
            suggestions.append((tag_name, f"//{tag_name}[@placeholder='{attrs['placeholder']}']"))
        elif tag.text.strip():
            suggestions.append((tag_name, f"//{tag_name}[text()='{tag.text.strip()}']"))

    return suggestions

def generate_script_from_suggestions(suggestions: list, url: str) -> str:
    """Generate a basic Selenium test script based on locator suggestions."""
    lines = [
        "from selenium import webdriver",
        "from selenium.webdriver.common.by import By",
        "",
        "def test_auto_generated():",
        "    driver = webdriver.Chrome()",
        f"    driver.get('{url}')",
        ""
    ]

    for tag, locator in suggestions:
        lines.append(f"    element = driver.find_element(By.XPATH, \"{locator}\")  # <{tag}>")

    lines.append("    driver.quit()")
    return "\n".join(lines)
