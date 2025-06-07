
from components.healer_runner import auto_heal_run

def test_autoheal_122():
    html = """<input name='username'>"""
    broken_locator = "//input[@name='username']"
    result = auto_heal_run(broken_locator, html, module="test_case_122")
    assert result is not None
