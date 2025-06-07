
from components.healer_runner import auto_heal_run

def test_autoheal_1847():
    html = """<button type='submit'>Submit</button>"""
    broken_locator = "//button[@type='submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_1847")
    assert result is not None
