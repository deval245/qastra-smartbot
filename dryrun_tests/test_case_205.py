
from components.healer_runner import auto_heal_run

def test_autoheal_205():
    html = """<span>Submit</span>"""
    broken_locator = "//span[text()='Submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_205")
    assert result is not None
