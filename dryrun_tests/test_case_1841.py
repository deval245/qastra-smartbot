
from components.healer_runner import auto_heal_run

def test_autoheal_1841():
    html = """<button type='submit'>Submit</button>"""
    broken_locator = "//button[@typ='submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_1841")
    assert result is not None
