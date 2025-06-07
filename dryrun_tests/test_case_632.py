
from components.healer_runner import auto_heal_run

def test_autoheal_632():
    html = """<a href='#'>Forgot password?</a>"""
    broken_locator = "//a[contains(text(), 'Forgot')]"
    result = auto_heal_run(broken_locator, html, module="test_case_632")
    assert result is not None
