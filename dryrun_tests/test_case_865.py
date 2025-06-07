
from components.healer_runner import auto_heal_run

def test_autoheal_865():
    html = """<div class='login-box'></div>"""
    broken_locator = "//div[@class='login-box']"
    result = auto_heal_run(broken_locator, html, module="test_case_865")
    assert result is not None
