
from components.healer_runner import auto_heal_run

def test_autoheal_1254():
    html = """<input type='email'>"""
    broken_locator = "//input[@type='email']"
    result = auto_heal_run(broken_locator, html, module="test_case_1254")
    assert result is not None
