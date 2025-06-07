
from components.healer_runner import auto_heal_run

def test_autoheal_1346():
    html = """<input placeholder='Enter email'>"""
    broken_locator = "//input[@placeholder='Enter email']"
    result = auto_heal_run(broken_locator, html, module="test_case_1346")
    assert result is not None
