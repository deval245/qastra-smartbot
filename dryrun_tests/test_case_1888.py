
from components.healer_runner import auto_heal_run

def test_autoheal_1888():
    html = """<button type='submit'>Submit</button>"""
    broken_locator = "//button[@type='submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_1888")
    assert result is not None
