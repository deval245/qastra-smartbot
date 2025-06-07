
from components.healer_runner import auto_heal_run

def test_autoheal_1778():
    html = """<a href='#'>Forgot password?</a>"""
    broken_locator = "//a[cntains(text(), 'Forgot')]"
    result = auto_heal_run(broken_locator, html, module="test_case_1778")
    assert result is not None
