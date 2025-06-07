
from components.healer_runner import auto_heal_run

def test_autoheal_189():
    html = """<label for='username'>Username</label>"""
    broken_locator = "//label[@for='username']"
    result = auto_heal_run(broken_locator, html, module="test_case_189")
    assert result is not None
