
from components.healer_runner import auto_heal_run

def test_autoheal_1917():
    html = """<form id='loginForm'></form>"""
    broken_locator = "//section[@id='loginForm']"
    result = auto_heal_run(broken_locator, html, module="test_case_1917")
    assert result is not None
