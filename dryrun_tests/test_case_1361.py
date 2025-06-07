
from components.healer_runner import auto_heal_run

def test_autoheal_1361():
    html = """<button type='submit'>Submit</button>"""
    broken_locator = "//button[@typ='submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_1361")
    assert result is not None
