
from components.healer_runner import auto_heal_run

def test_autoheal_680():
    html = """<span>Submit</span>"""
    broken_locator = "//span[text()='Submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_680")
    assert result is not None
