
from components.healer_runner import auto_heal_run

def test_autoheal_264():
    html = """<input type='email'>"""
    broken_locator = "//input[@type='email']"
    result = auto_heal_run(broken_locator, html, module="test_case_264")
    assert result is not None
