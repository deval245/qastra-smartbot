
from components.healer_runner import auto_heal_run

def test_autoheal_448():
    html = """<button type='submit'>Submit</button>"""
    broken_locator = "//button[@type='submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_448")
    assert result is not None
