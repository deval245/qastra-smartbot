
from components.healer_runner import auto_heal_run

def test_autoheal_967():
    html = """<input name='username'>"""
    broken_locator = "//input[@name='username']"
    result = auto_heal_run(broken_locator, html, module="test_case_967")
    assert result is not None
