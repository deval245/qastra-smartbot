import os
import random

TEST_FOLDER = "dryrun_tests"
os.makedirs(TEST_FOLDER, exist_ok=True)

base_locators = [
    ("//*[@id='user_login']", "<input id='user_login' placeholder='Enter email'>"),
    ("//input[@name='username']", "<input name='username'>"),
    ("//input[@type='email']", "<input type='email'>"),
    ("//button[@type='submit']", "<button type='submit'>Submit</button>"),
    ("//a[contains(text(), 'Forgot')]", "<a href='#'>Forgot password?</a>"),
    ("//div[@class='login-box']", "<div class='login-box'></div>"),
    ("//span[text()='Submit']", "<span>Submit</span>"),
    ("//label[@for='username']", "<label for='username'>Username</label>"),
    ("//input[@placeholder='Enter email']", "<input placeholder='Enter email'>"),
    ("//form[@id='loginForm']", "<form id='loginForm'></form>")
]

def corrupt_locator(locator):
    corruptions = [
        lambda x: x.replace("id", "idd"),
        lambda x: x.replace("name", "nam"),
        lambda x: x.replace("type", "typ"),
        lambda x: x.replace("text()", "txt()"),
        lambda x: x.replace("contains", "cntains"),
        lambda x: x.replace("input", "div"),
        lambda x: x.replace("button", "span"),
        lambda x: x.replace("form", "section"),
        lambda x: x.replace("label", "span"),
        lambda x: x.replace("placeholder", "placehldr")
    ]
    return random.choice(corruptions)(locator)

for i in range(2000):
    locator, html = random.choice(base_locators)
    broken_locator = corrupt_locator(locator)

    filename = f"test_case_{i+1}.py"
    filepath = os.path.join(TEST_FOLDER, filename)

    with open(filepath, "w") as f:
        f.write(f"""
from components.healer_runner import auto_heal_run

def test_autoheal_{i+1}():
    html = \"\"\"{html}\"\"\"
    broken_locator = \"{broken_locator}\"
    result = auto_heal_run(broken_locator, html, module="test_case_{i+1}")
    assert result is not None
""")

