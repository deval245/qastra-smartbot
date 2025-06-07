
from components.healer_runner import auto_heal_run

def test_autoheal_1757():
    html = """<span>Submit</span>"""
    broken_locator = "//span[txt()='Submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_1757")
    assert result is not None
