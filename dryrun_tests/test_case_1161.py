
from components.healer_runner import auto_heal_run

def test_autoheal_1161():
    html = """<input name='username'>"""
    broken_locator = "//input[@nam='usernam']"
    result = auto_heal_run(broken_locator, html, module="test_case_1161")
    assert result is not None
