
from components.healer_runner import auto_heal_run

def test_autoheal_1371():
    html = """<input name='username'>"""
    broken_locator = "//div[@name='username']"
    result = auto_heal_run(broken_locator, html, module="test_case_1371")
    assert result is not None
