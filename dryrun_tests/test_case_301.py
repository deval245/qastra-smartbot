
from components.healer_runner import auto_heal_run

def test_autoheal_301():
    html = """<input name='username'>"""
    broken_locator = "//input[@nam='usernam']"
    result = auto_heal_run(broken_locator, html, module="test_case_301")
    assert result is not None
