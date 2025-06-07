
from components.healer_runner import auto_heal_run

def test_autoheal_1017():
    html = """<label for='username'>Username</label>"""
    broken_locator = "//label[@for='usernam']"
    result = auto_heal_run(broken_locator, html, module="test_case_1017")
    assert result is not None
