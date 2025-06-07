
from components.healer_runner import auto_heal_run

def test_autoheal_1102():
    html = """<form id='loginForm'></form>"""
    broken_locator = "//form[@id='loginForm']"
    result = auto_heal_run(broken_locator, html, module="test_case_1102")
    assert result is not None
