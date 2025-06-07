
from components.healer_runner import auto_heal_run

def test_autoheal_1798():
    html = """<input type='email'>"""
    broken_locator = "//div[@type='email']"
    result = auto_heal_run(broken_locator, html, module="test_case_1798")
    assert result is not None
