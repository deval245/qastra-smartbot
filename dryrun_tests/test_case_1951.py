
from components.healer_runner import auto_heal_run

def test_autoheal_1951():
    html = """<form id='loginForm'></form>"""
    broken_locator = "//form[@id='loginForm']"
    result = auto_heal_run(broken_locator, html, module="test_case_1951")
    assert result is not None
