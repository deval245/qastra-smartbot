
from components.healer_runner import auto_heal_run

def test_autoheal_1303():
    html = """<div class='login-box'></div>"""
    broken_locator = "//div[@class='login-box']"
    result = auto_heal_run(broken_locator, html, module="test_case_1303")
    assert result is not None
