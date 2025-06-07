
from components.healer_runner import auto_heal_run

def test_autoheal_564():
    html = """<label for='username'>Username</label>"""
    broken_locator = "//label[@for='username']"
    result = auto_heal_run(broken_locator, html, module="test_case_564")
    assert result is not None
