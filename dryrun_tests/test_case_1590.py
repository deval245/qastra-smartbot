
from components.healer_runner import auto_heal_run

def test_autoheal_1590():
    html = """<a href='#'>Forgot password?</a>"""
    broken_locator = "//a[contains(text(), 'Forgot')]"
    result = auto_heal_run(broken_locator, html, module="test_case_1590")
    assert result is not None
