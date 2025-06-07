
from components.healer_runner import auto_heal_run

def test_autoheal_1296():
    html = """<input name='username'>"""
    broken_locator = "//input[@name='username']"
    result = auto_heal_run(broken_locator, html, module="test_case_1296")
    assert result is not None
