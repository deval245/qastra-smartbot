
from components.healer_runner import auto_heal_run

def test_autoheal_533():
    html = """<button type='submit'>Submit</button>"""
    broken_locator = "//span[@type='submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_533")
    assert result is not None
