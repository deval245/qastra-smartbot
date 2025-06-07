
from components.healer_runner import auto_heal_run

def test_autoheal_1237():
    html = """<button type='submit'>Submit</button>"""
    broken_locator = "//button[@type='submit']"
    result = auto_heal_run(broken_locator, html, module="test_case_1237")
    assert result is not None
