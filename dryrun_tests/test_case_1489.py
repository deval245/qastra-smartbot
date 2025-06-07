
from components.healer_runner import auto_heal_run

def test_autoheal_1489():
    html = """<label for='username'>Username</label>"""
    broken_locator = "//span[@for='username']"
    result = auto_heal_run(broken_locator, html, module="test_case_1489")
    assert result is not None
