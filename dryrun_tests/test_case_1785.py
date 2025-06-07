
from components.healer_runner import auto_heal_run

def test_autoheal_1785():
    html = """<input type='email'>"""
    broken_locator = "//input[@typ='email']"
    result = auto_heal_run(broken_locator, html, module="test_case_1785")
    assert result is not None
