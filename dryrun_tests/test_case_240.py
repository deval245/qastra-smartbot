
from components.healer_runner import auto_heal_run

def test_autoheal_240():
    html = """<input type='email'>"""
    broken_locator = "//input[@typ='email']"
    result = auto_heal_run(broken_locator, html, module="test_case_240")
    assert result is not None
