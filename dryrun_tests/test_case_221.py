
from components.healer_runner import auto_heal_run

def test_autoheal_221():
    html = """<label for='username'>Username</label>"""
    broken_locator = "//label[@for='usernam']"
    result = auto_heal_run(broken_locator, html, module="test_case_221")
    assert result is not None
