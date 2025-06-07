
from components.healer_runner import auto_heal_run

def test_autoheal_223():
    html = """<input placeholder='Enter email'>"""
    broken_locator = "//input[@placeholder='Enter email']"
    result = auto_heal_run(broken_locator, html, module="test_case_223")
    assert result is not None
