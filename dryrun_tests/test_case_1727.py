
from components.healer_runner import auto_heal_run

def test_autoheal_1727():
    html = """<input placeholder='Enter email'>"""
    broken_locator = "//div[@placeholder='Enter email']"
    result = auto_heal_run(broken_locator, html, module="test_case_1727")
    assert result is not None
