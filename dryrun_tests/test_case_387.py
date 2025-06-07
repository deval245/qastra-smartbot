
from components.healer_runner import auto_heal_run

def test_autoheal_387():
    html = """<input placeholder='Enter email'>"""
    broken_locator = "//input[@placehldr='Enter email']"
    result = auto_heal_run(broken_locator, html, module="test_case_387")
    assert result is not None
